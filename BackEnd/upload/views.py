import json
from django.http.response import JsonResponse
from rest_framework.generics import ListAPIView
from BackEnd.settings import BASE_DIR,SOURCE_FILE_PATH,INPUT_FILE_PATH
from FuzzAll.fuzz import fuzz_one
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
# from django.views.generic.base import TemplateView, View
from .models import *
import os
from .analyze import Analyze
from .ser import UsedSoftSer
# import _thread
# Create your views here.



def threadFuzz(fuzzer, program_path, isqemu, ins, outs, params, isfile, codeOrProgramBoolean: bool, codeOrProgram,compileCommand,programName):
    result = fuzz_one(fuzzer=fuzzer, program_path=program_path,
                      isqemu=False, ins=ins, outs=outs, params=params, isfile=isfile,compileCommand=compileCommand,programName=programName)
    # if codeOrProgramBoolean:
    #     codeResult.objects.create(codeCoverage=result['codeCoverage'],
    #                       bugs=result['bugs'], sample=result['sample'], code=codeOrProgram)
    # else:
    #     programResult.objects.create(
    #         codeCoverage=result['codeCoverage'], bugs=result['bugs'], sample=result['sample'], code=codeOrProgram)
    pass


def sourceCode(request):
    if request.method == 'POST':
        print(request.POST)
        filePath = request.POST.get("fileList", None)
        analyze = Analyze(filePath)
        filePath = analyze.Unzip()#解压缩
        name = request.POST.get('name','mem')
        seed = request.POST.get('seed',None)
        inputFile = request.POST.get('inputFile', None)
        if inputFile == None:
            pass
        else:
            inputFile = os.path.join(INPUT_FILE_PATH,inputFile)
        parameter = request.POST.get('parameter',None)
        compileCommand = request.POST.get('compileCommand',None)
        inputCommand = request.POST.get('inputCommand',None)
        programName = request.POST.get("programName",None)
        outs = os.path.join("/root/fuzzResult/",programName)
        print('获取信息成功')
        if seed == None and inputFile == None:
            return HttpResponse("没有选择种子文件")
        if not filePath:
            return HttpResponse("no files for upload!")
        else:
            isfile = False
            temp = uploadSourceCode.objects.create(
                filePath=filePath, name=name, ins=seed, inputFile=inputFile, parameter=parameter, compileCommand=compileCommand, inputCommand=inputCommand)
            temp.save()
            if not inputFile:
                isfile = True
                threadFuzz(
                    fuzzer=name, program_path=str(filePath), isqemu=False, ins=seed, outs=outs, params=parameter, isfile=isfile,codeOrProgramBoolean=True,codeOrProgram=temp,compileCommand=compileCommand,programName=programName)
            else:
                # 调用接口传数据
                threadFuzz(
                    fuzzer=name, program_path=str(filePath), isqemu=False, ins=inputFile, outs=outs, params=parameter, isfile=isfile,codeOrProgramBoolean=True,codeOrProgram=temp,compileCommand=compileCommand,programName=programName)

            return JsonResponse({"msg":"成功提交，请耐心等待结果"})


def sourceProgram(request):
    if request.method == 'POST':
        print(request.POST)
        filePath = request.POST.get("fileList", None)
        name = request.POST['name']
        seed = request.POST['seed']
        inputFile = request.POST.get('inputFile', None)
        parameter = request.POST['parameter']
        compileCommand = request.POST['compileCommand']
        compileExample = """CC=/home/minipython/桌面/AggregateFuzzing/
        BackEnd/tools/afl/mm_metric/afl-clang-fast CXX=/home/minipython/桌面/AggregateFuzzing/BackEnd/
        tools/afl/mm_metric/afl-clang-fast++ ./configure"""
        inputCommand = request.POST.get('inputCommand',"@@")
        outs = os.path.join(BASE_DIR, 'outs')

        print('test')
        if not filePath:
            return HttpResponse("no files for upload!")
        else:
            isfile = False
            temp = uploadSourceProgram.objects.create(
                filePath=filePath, name=name, ins=seed, inputFile=inputFile, parameter=parameter, inputCommand=inputCommand)
            ##路径替换
            ext = str(filePath).split('.')[-1]
            filePath = '/'.join([os.getcwd(), 'sourceTotal', str(filePath).strip('.'+ext), str(filePath)])

            extInput= str(inputFile).split('.')[-1]
            inputFile = '/'.join([os.getcwd(), 'inputFile', str(inputFile).strip('.'+extInput)])
            print(str(filePath),str(inputFile))
            if not inputFile:
                isfile = True
                threadFuzz(
                    fuzzer=name, program_path=str(filePath), isqemu=False, ins=inputFile, outs=outs, params=parameter, isfile=isfile,codeOrProgramBoolean=True,codeOrProgram=temp,compileCommand=compileCommand)
            else:
                # 调用接口传数据
                threadFuzz(
                    fuzzer=name, program_path=str(filePath), isqemu=False, ins=inputFile, outs=outs, params=parameter, isfile=isfile,codeOrProgramBoolean=True,codeOrProgram=temp,compileCommand=compileCommand)

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
            print("dic[%s]=%s" %(k,v))
            fileData = request.FILES.getlist(k)
            for file in fileData:
                fileName = file._get_name()
                
                filePath = os.path.join(SOURCE_FILE_PATH, fileName)
                print('filepath = [%s]'%filePath)
                os.system("mkdir %s" %(SOURCE_FILE_PATH))
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
