from FuzzAll.fuzz import fuzz_one
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import TemplateView, View
from .models import *
import os
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'index.html'


def sourceCode(request):
    if request.method == 'GET':
        seedList = ''
        with open('seed.txt','r') as f:
            seedList = f.readlines()
        f.close()
        return render(request, 'sourceCode/sourceCode.html',{'seedList':seedList})
    elif request.method == 'POST':
        print(request.POST)
        filePath = request.FILES.get("myfile", None)
        name = request.POST['name']
        seed = request.POST['seed']
        inputFile = request.FILES.get('inputFile',None)
        parameter = request.POST['parameter']
        compileCommand = request.POST['compileCommand']
        inputCommand = request.POST['inputCommand']
        fuzz_one()
        if not filePath:
            return HttpResponse("no files for upload!")
        else:
            ifile = False
            if not inputFile:
                ifile = True
            else:
                # 调用接口传数据
                uploadSourceCode.objects.create(
                    filePath=filePath, name=name, parameter=parameter)
                return render(request, 'sourceCode/wait.html')


def sourceProgram(request):
    if request.method == 'GET':
        return render(request, 'sourceProgram/sourceProgram.html')
    elif request.method == 'POST':
        print(request.POST)
        filePath = request.FILES.get("myfile", None)
        name = request.POST['name']
        parameter = request.POST['parameter']
        compileCommand = request.POST['compileCommand']
        if not filePath:
            return HttpResponse("no files for upload!")
        else:
            # 调用接口传数据
            uploadSourceProgram.objects.create(
                filePath=filePath, name=name, parameter=parameter, compileCommand=compileCommand)
            return render(request, 'sourceCode/wait.html')
