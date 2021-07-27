from datetime import datetime
from Util.decompress import cd, pathJoin,sum_table_data,invi_table_data
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
import json
def threadFuzz(fuzzer, program_path, isqemu, ins, outs, prePara, postPara,isfile, codeOrProgramBoolean: bool, codeOrProgram,compileCommand,programName,hour,minute,id):
    result = fuzz_one(fuzzer=fuzzer, program_path=program_path,
                      isqemu=False, ins=ins, outs=outs, prePara=prePara, postPara=postPara,isfile=isfile,compileCommand=compileCommand,programName=programName,hour = hour,minute = minute, id = id)

    return result


def sourceCode(request):
    if request.method == 'POST':
        print(request.POST)
        filePath = request.POST.get("fileList", None)
        analyze = Analyze(filePath)
        filePath = analyze.Unzip()#解压缩
        seed = request.POST.get('seed',None)
        inputFile = request.POST.get('inputFile', None)
        if inputFile == None:
            pass
        else:
            inputFile = os.path.join(INPUT_FILE_PATH,inputFile)
        prePara = request.POST.get('prePara',None)
        postPara = request.POST.get('postPara',None)
        compileCommand = request.POST.get('compileCommand',"")
        inputCommand = request.POST.get('inputCommand',None)
        programName = request.POST.get("programName",None)
        hour = request.POST.get("hour",0)
        minute = request.POST.get("minute",25)
        resultTime = ""
        for name in ["AFLPLUSPLUS","MEMAFL","TORTOISE"]: #AFL"MEMAFL","AFLPLUSPLUS","TORTOISE"
            outs = os.path.join("/root/fuzzResult/",name,programName)
            try:
                os.mkdir(pathJoin("/root/fuzz_target",name))
            except:
                pass
            copyCMD = "cp -r %s %s"%(filePath,pathJoin("/root/fuzz_target",name))
            print(copyCMD)
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
                    filePath=filePath, name=name, ins=seed, inputFile=inputFile, prePara=prePara, postPara=postPara,compileCommand=compileCommand, inputCommand=inputCommand)
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
        print(request.POST)
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
    # def result(request):
    #     if request.method == "POST":
    #         programName = request.POST.get("id",None)
    #         if not programName:
    #             response = HttpResponse()
    #             response.content = "没有参数提供"
    #             response.status_code = 412
    #             return response
    #     elif request.method == "GET":
    serializer_class = ResultSer
    queryset = codeResult.objects.all()
                

        
def process(request):
    if request.method == "POST":
        fuzzers  = ["MEM","AFLPP","TORTOISE"]
        programName = request.POST.get("programName",None)
        if not programName :
            response = HttpResponse()
            response.content = "没有参数提供"
            response.status_code = 412
            return response
        else:
            
            code_list = codeResult.objects.filter(programName = programName)
            print(code_list)
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
                sum_ms = (datetime.strptime(code.time,"%Y-%m-%d %H:%M:%S") - datetime.now()).seconds *1000
                data_send[code.fuzzer] = result_individual
                data_send[code.fuzzer+"_sum"] = result_summary
            data_send["sum_ms"] = sum_ms
            print(data_send)
            return HttpResponse(json.dumps(data_send), content_type='application/json')
                # return JsonResponse(data = json.dumps(mem),safe=False)


def download(request):
    if request.method == "POST":
        print(request.POST)
        codeResult_id = request.POST.get("id",None)
        print(codeResult_id)
        if id == None:
            return HttpResponseNotAllowed

        codeResultInstance = codeResult.objects.get(id = codeResult_id)
        cd("/root/test")
        zipCMD = "7za a -tzip -r %s.zip %s"%(codeResultInstance.programName+codeResultInstance.fuzzer,
        pathJoin(DIRS[codeResultInstance.fuzzer],codeResultInstance.programName))
        run(zipCMD,shell= True)
        file_path = codeResultInstance.programName+".zip"
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
            print(serializer.data)
            return JsonResponse(serializer.data, safe=False)
        except:
            # print("dsjfklasdjflksadjfklsadjkfjadsf")
            return 
