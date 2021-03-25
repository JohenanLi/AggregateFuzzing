from BackEnd.settings import BASE_DIR
from FuzzAll.fuzz import fuzz_one
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import TemplateView, View
from .models import *
import os
import _thread
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'index.html'


def threadFuzz(fuzzer, program_path, isqemu, ins, outs, params, isfile, codeOrProgramBoolean: bool, codeOrProgram,compileCommand):
    result = fuzz_one(fuzzer=fuzzer, program_path=program_path,
                      isqemu=False, ins=ins, outs=outs, params=params, isfile=isfile,compileCommand=compileCommand)
    # if codeOrProgramBoolean:
    #     codeResult.objects.create(codeCoverage=result['codeCoverage'],
    #                       bugs=result['bugs'], sample=result['sample'], code=codeOrProgram)
    # else:
    #     programResult.objects.create(
    #         codeCoverage=result['codeCoverage'], bugs=result['bugs'], sample=result['sample'], code=codeOrProgram)
    pass


def sourceCode(request):
    if request.method == 'GET':
        seedList = ''
        with open('seed.txt', 'r') as f:
            seedList = f.readlines()
        f.close()
        return render(request, 'sourceCode/sourceCode.html', {'seedList': seedList})
    elif request.method == 'POST':
        print(request.POST)
        filePath = request.FILES.get("myfile", None)
        
        name = request.POST['name']
        seed = request.POST.get('seed',None)
        inputFile = request.FILES.get('inputFile', None)
        parameter = request.POST.get('parameter',None)
        compileCommand = request.POST.get('compileCommand',None)
        inputCommand = request.POST.get('inputCommand',None)
        outs = os.path.join(BASE_DIR, 'outs')

        print('test')
        if not filePath:
            return HttpResponse("no files for upload!")
        else:
            isfile = False
            temp = uploadSourceCode.objects.create(
                filePath=filePath, name=name, ins=seed, inputFile=inputFile, parameter=parameter, compileCommand=compileCommand, inputCommand=inputCommand)
            temp.save()
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

            return render(request, 'sourceCode/wait.html', {'object': temp})


def sourceProgram(request):
    if request.method == 'GET':
        seedList = ''
        with open('seed.txt', 'r') as f:
            seedList = f.readlines()
        f.close()
        return render(request, 'sourceProgram/sourceProgram.html', {'seedList': seedList})
    elif request.method == 'POST':
        print(request.POST)
        filePath = request.FILES.get("myfile", None)
        name = request.POST['name']
        seed = request.POST['seed']
        inputFile = request.FILES.get('inputFile', None)
        parameter = request.POST['parameter']
        compileCommand = request.POST['compileCommand']
        compileExample = """CC=/home/minipython/桌面/AggregateFuzzing/
        BackEnd/tools/afl/mm_metric/afl-clang-fast CXX=/home/minipython/桌面/AggregateFuzzing/BackEnd/
        tools/afl/mm_metric/afl-clang-fast++ ./configure"""
        inputCommand = request.POST['inputCommand']
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
