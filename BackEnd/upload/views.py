from datetime import datetime, timedelta
import subprocess
from Util.decompress import cd, pathJoin, pwd,sum_table_data,invi_table_data
from django.http.response import  HttpResponseNotAllowed, JsonResponse
from rest_framework.generics import ListAPIView
from BackEnd.settings import BASE_DIR,SOURCE_FILE_PATH,INPUT_FILE_PATH,SEED_PATH
from FuzzAll.fuzz import ALL_PATHS, DIRS, fuzz_one
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import *
import os
from .analyze import Analyze
from .ser import UsedSoftSer
from subprocess import getoutput, run
from FuzzAll.config import MEM_AFL_PATH
from .models import codeResult
from .ser import ResultSer
from rest_framework import viewsets
from rest_framework.views import APIView
from django.db.models import Q
from Util.translate import fuzzer_trans
import json
from jinja2 import Environment, FileSystemLoader


def threadFuzz(fuzzer, program_path, isqemu, ins, outs, prePara, postPara,isfile, codeOrProgramBoolean: bool, codeOrProgram,compileCommand,programName,hour,minute,id):
    result = fuzz_one(fuzzer=fuzzer, program_path=program_path,
                      isqemu=False, ins=ins, outs=outs, prePara=prePara, postPara=postPara,isfile=isfile,compileCommand=compileCommand,
                      programName=programName,hour = hour,minute = minute, id = id)

    return result


def sourceCode(request):#参数获取模块
    if request.method == 'POST':
        filePath = request.POST.get("fileList", None)
        analyze = Analyze(filePath)
        filePath = analyze.Unzip()#解压缩
        seed = request.POST.get('seed',None)
        inputFile = request.POST.get('inputFile', None)
        if inputFile == None:
            pass
        else:
            inputFile = os.path.join(INPUT_FILE_PATH,inputFile)
        programName = request.POST.get("programName",None)
        prePara = request.POST.get('prePara',None)
        postPara = request.POST.get('postPara',None)
        if programName == "pdftopng":
            prePara = "-mono"
            postPara = "o"
        elif programName == "pdftotext":
            prePara = "-lineprinter"
            postPara = "o"
        elif programName == "pdftoppm":
            prePara = "-mono"
            postPara = "o"
        compileCommand = request.POST.get('compileCommand',"")
        inputCommand = request.POST.get('inputCommand',None)
        
        hour = request.POST.get("hour",0)
        minute = request.POST.get("minute",25)
        resultTime = ""
        for name in ["MEMAFL","TORTOISE","DRILLER"]: 
            outs = os.path.join("/root/fuzzResult/",name,programName)
            try:
                os.mkdir(pathJoin("/root/fuzz_target",name))
            except:
                pass
            copyCMD = "cp -r %s %s"%(filePath,pathJoin("/root/fuzz_target",name))
            filePathList = filePath.split("/")
            filePath = pathJoin("/root/fuzz_target",name,filePathList[-1])
            run(copyCMD,shell = True)
            print('获取信息成功')
            if seed == None and inputFile == None:
                response = HttpResponse()
                response.content = "没有上传种子文件"
                response.status_code = 412
                return response
            if not filePath:
                response = HttpResponse()
                response.content = "没有上传源代码文件!"
                response.status_code = 412
                return response
            else:
                isfile = False
                temp = uploadSourceCode.objects.create(
                    filePath=filePath, name=name, ins=seed, inputFile=inputFile, prePara=prePara, 
                    postPara=postPara,compileCommand=compileCommand, 
                    inputCommand=inputCommand,minute = minute ,hour = hour)
                temp.save()
                if not inputFile:
                    isfile = True
                    resultTime =threadFuzz(
                        fuzzer=name, program_path=str(filePath), isqemu=False, ins=pathJoin(SEED_PATH,seed), outs=outs, prePara=prePara, postPara=postPara,isfile=isfile,codeOrProgramBoolean=True,codeOrProgram=temp,compileCommand=compileCommand,programName=programName,hour = hour,minute = minute,id = temp.id)
                else:
                    # 调用接口传数据
                    resultTime = threadFuzz(
                        fuzzer=name, program_path=str(filePath), isqemu=False, ins=inputFile, outs=outs, prePara=prePara, postPara=postPara,isfile=isfile,codeOrProgramBoolean=True,codeOrProgram=temp,compileCommand=compileCommand,programName=programName,hour = hour, minute = minute,id = temp.id)

    
        return JsonResponse({"msg":resultTime,"sum_ms":(int(hour)*60*60+int(minute)*60) *1000})


def sourceProgram(request):
    if request.method == 'POST':
        filePath = request.POST.get("fileList", None)
        name = request.POST['name']
        seed = request.POST['seed']
        inputFile = request.POST.get('inputFile', None)
        prePara = request.POST.get('prePara',None)
        compileCommand = request.POST['compileCommand']
        inputCommand = request.POST.get('inputCommand',"@@")
        outs = os.path.join(BASE_DIR, 'outs')

        print('test')
        if not filePath:
            return HttpResponse("no files for upload!")
        else:
            isfile = False
            temp = uploadSourceProgram.objects.create(
                filePath=filePath, name=name, ins=seed, inputFile=inputFile, prePara=prePara, inputCommand=inputCommand)
            
            ##路径替换
            ext = str(filePath).split('.')[-1]
            filePath = '/'.join([os.getcwd(), 'sourceTotal', str(filePath).strip('.'+ext), str(filePath)])

            extInput= str(inputFile).split('.')[-1]
            inputFile = '/'.join([os.getcwd(), 'inputFile', str(inputFile).strip('.'+extInput)])
            print(str(filePath),str(inputFile))
            if not inputFile:
                isfile = True
                threadFuzz(
                    fuzzer=name, program_path=str(filePath), isqemu=False, ins=inputFile, outs=outs, prePara=prePara, isfile=isfile,codeOrProgramBoolean=True,codeOrProgram=temp,compileCommand=compileCommand)
            else:
                # 调用接口传数据
                threadFuzz(
                    fuzzer=name, program_path=str(filePath), isqemu=False, ins=inputFile, outs=outs, prePara=prePara, isfile=isfile,codeOrProgramBoolean=True,codeOrProgram=temp,compileCommand=compileCommand)

                return render(request, 'sourceProgram/wait.html', {object: temp})

def writeFile(filePath, file):
    # print(os.system("> "+ filePath))
    with open(filePath, "wb") as f:
        if file.multiple_chunks():
            for content in file.chunks():
                f.write(content)
        else:
            data=file.read() ###.decode('utf-8')
            f.write(data)

def uploadCode(request):
    if request.method == "POST":  
        fileDict = request.FILES.items()
        print(fileDict)
        fileList = []
        # 获取上传的文件，如果没有文件，则默认为None    
        if not fileDict:
            return JsonResponse({'msg': 'no file upload'})
        for (k, v) in fileDict:
            # print("dic[%s]=%s" %(k,v))
            fileData = request.FILES.getlist(k)
            for file in fileData:
                fileName = file._get_name()
                # fileName = fileName.strip("0123456789-")
                # print(fileName)
                filePath = os.path.join(SOURCE_FILE_PATH, fileName)
                # print('filepath = [%s]'%filePath)
                # os.system("mkdir %s" %(SOURCE_FILE_PATH))
                fileList.append(filePath)
                try:
                    writeFile(filePath, file)
                except:
                    return JsonResponse({'msg': 'file write failed'})
        
        return JsonResponse({'msg': 'success','file_path':fileList})

def uploadInputFile(request):
    if request.method == "POST":  
        fileDict = request.FILES.items()
        fileList = []
        # 获取上传的文件，如果没有文件，则默认为None    
        if not fileDict:
            return JsonResponse({'msg': 'no file upload'})
        for (k, v) in fileDict:
            print("dic[%s]=%s" %(k,v))
            fileData = request.FILES.getlist(k)
            for file in fileData:
                fileName = file._get_name()
                ext = fileName.split('.')[-1]
                filePath = os.path.join(INPUT_FILE_PATH, ext,fileName)

                print('filepath = [%s]'%ext)
                fileList.append(ext)
                try:
                    os.system("mkdir %s" %(INPUT_FILE_PATH))
                    os.system("mkdir "+os.path.join(INPUT_FILE_PATH,ext))
                    writeFile(filePath, file)
                except:
                    return JsonResponse({'msg': 'file write failed'})
        return JsonResponse({'msg': 'success','inputFile':fileList})

class AvailList(ListAPIView):
    serializer_class = UsedSoftSer
    queryset  = usedSoft.objects.all()

def getExts(request):
    if request.method == "GET":
        exts = []
        with open("seed.txt","r") as f:
            for line in f.readlines():
                exts.append(line.rstrip())
            return JsonResponse(exts,safe=False)

class ResultViewSet(viewsets.ModelViewSet):
    serializer_class = ResultSer
    queryset = codeResult.objects.all()
                

        
def process(request):#将引擎的实时运行状况反馈到等待页面
    if request.method == "POST":
        fuzzers  = ["MEM","DRILLER","TORTOISE"]
        programName = request.POST.get("programName",None)
        if not programName :
            response = HttpResponse()
            response.content = "没有参数提供"
            response.status_code = 412
            return response
        else:
            
            code_list = codeResult.objects.filter(programName = programName)
            sourceCodeInstance = code_list[0].code
            # print(code_list)
            data_send = {}
            sum_ms = ""
            for code in code_list:
                # codeResultInstance = codeResult.objects.get(id = id)
                whatsup_individual = pathJoin(MEM_AFL_PATH,"afl-whatsup_individual")
                whatsup_summary = pathJoin(MEM_AFL_PATH,"afl-whatsup_summary")
                outs = pathJoin("/root/fuzzResult",code.fuzzer,code.programName)
                result_individual =  invi_table_data(getoutput(whatsup_individual+" "+outs))
                if result_individual == -1:
                    response = HttpResponse()
                    response.status_code = 500
                    return response
                result_summary = sum_table_data(getoutput(whatsup_summary+" "+outs))
                data_send[code.fuzzer] = result_individual
                data_send[code.fuzzer+"_sum"] = result_summary
            tempTime = datetime.strptime(code_list[0].time,"%Y-%m-%d %H:%M:%S") + timedelta(
                    minutes=float(sourceCodeInstance.minute),hours=float(sourceCodeInstance.hour))
            sum_ms = ( tempTime- datetime.now()).seconds *1000
            data_send["sum_ms"] = sum_ms
            data_send["timeOk"] = tempTime.strftime("%Y-%m-%d %H:%M:%S")
            # print(data_send)
            return HttpResponse(json.dumps(data_send), content_type='application/json')


def download(request):#下载详细结果,用于调试程序记录栈回溯并打包测试结果文件
    if request.method == "POST":
        print(request.POST)
        codeResult_id = request.POST.get("id",None)
        print(codeResult_id)
        if id == None:
            return HttpResponseNotAllowed

        codeResultInstance = codeResult.objects.get(id = codeResult_id)
        with open("/root/AggregateFuzzing/BackEnd/Util/dir.txt","w") as f:
            f.write(os.path.join("/root/fuzzResult",codeResultInstance.fuzzer,
            codeResultInstance.programName))
            f.close()

        subprocess.run("gdb -q -x /root/AggregateFuzzing/BackEnd/Util/new_gdb_info.py",shell=True)
        fuzzer_trans(os.path.join("/root/fuzzResult",codeResultInstance.fuzzer,
            codeResultInstance.programName))
        cd("/root/test")
        zipCMD = "7za a -tzip -r %s.zip %s"%(codeResultInstance.programName+codeResultInstance.fuzzer,
        pathJoin(DIRS[codeResultInstance.fuzzer],codeResultInstance.programName))
        run(zipCMD,shell= True)
        file_path = codeResultInstance.programName+codeResultInstance.fuzzer+".zip"
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    elif request.method == "GET":
        print("GET")

class fullSearchView(APIView):
    """
    搜索View，只需要关键词
    """
    def post(self,request):
        try:
            content = request.POST.get('content')
            error_msg = ''
            if not content:
                error_msg = "请输入关键词"
                return JsonResponse({'error_msg': error_msg})
            
            queryset = codeResult.objects.filter(Q(fuzzer__icontains=content)|Q(programName__icontains=content)|Q(time__icontains=content))
            serializer = ResultSer(instance=queryset, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return 

from subprocess import getstatusoutput
import os
def crash_analyze(request):#漏洞分析模块
    codeResult_id = request.POST.get("id",None)
    codeResultInstance = codeResult.objects.filter(id = codeResult_id).first()
    codeResult_list = [codeResultInstance]
    gdb_info_lines = []
    traceUtils = []
    bug_num = 0
    for one_codeResult in codeResult_list:
        dir = os.path.join("/root/fuzzResult",one_codeResult.fuzzer,one_codeResult.programName)
        
        engine_dict = {}
        fuzzer_str = ""
        stack_str = ""
        for root,dirs,files in os.walk(dir):
            if "fuzzer_stats" in files:
                f = open(root+"/fuzzer_stats","r")
                fuzzer_lines = f.readlines()
                fuzzer_lines = "".join(fuzzer_lines)
                fuzzer_lines = fuzzer_lines.replace("\n","<br>")
                # gdb_info_lines.append(fuzzer_lines + "<br>")
                fuzzer_str += fuzzer_lines + "<br>"
                f.close()
            if "gdb_info" in root and dirs == []:
                for file in files:
                    f = open(os.path.join(root,file),"r")
                    temp = os.path.join(root,file) +"<br>"
                    lines = f.readlines()
                    temp_tuple = [trace.split(' ')[2] for trace in lines[:-1]]
                    
                    if temp_tuple not in traceUtils:
                        bug_num += 1
                        traceUtils.append(temp_tuple)
                        
                        temp += "".join(lines)
                        

                        temp = temp.replace("\n","<br>")
                        stack_str += temp + "<br>"
                    f.close()
        engine_dict["fuzzer_stats"] = fuzzer_str
        engine_dict["stack_str"] = stack_str
        gdb_info_lines.append(engine_dict)
    path = "/root/AggregateFuzzing/BackEnd/Util"
    print(gdb_info_lines)
    # 创建一个加载器, jinja2 会从这个目录中加载模板
    loader = FileSystemLoader(path)

    # 用加载器创建一个环境, 有了它才能读取模板文件
    env = Environment(loader=loader)

    # 调用 get_template() 方法加载模板并返回
    template = env.get_template('demo.html')

    # 用 render() 方法渲染模板
    # 可以传递参数

    render_res = template.render(fuzzer=one_codeResult.fuzzer,gdb_info = gdb_info_lines,bug=bug_num)
    file_path = os.path.join("/root/fuzzResult",codeResultInstance.fuzzer,
    codeResultInstance.programName,"总结.html")
    with open(file_path,"w") as f:
        f.write(render_res)
        f.close()

    response = FileResponse(open(file_path, 'rb'))
    response['content_type'] = "application/octet-stream"
    response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
    return response