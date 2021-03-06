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
        return render(request, 'sourceCode/sourceCode.html')
    elif request.method == 'POST':
        filePath = request.FILES.get("myfile", None)
        name = request.POST['name']
        parameter = request.POST['parameter']
        if not filePath:
            return HttpResponse("no files for upload!")
        else:
            # 调用接口传数据
            uploadSourceCode.objects.create(
                filePath=filePath, name=name, parameter=parameter)
            return render(request, 'sourceCode/wait.html')


def sourceProgram(request):
    if request.method == 'GET':
        return render(request, 'sourceProgram/sourceProgram.html')
    elif request.method == 'POST':
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


# def upload_file(request):
#     if request.method == "POST":    # 请求方法为POST时，进行处理
#         myFile = request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
#         if not myFile:
#             return HttpResponse("no files for upload!")
#         # 打开特定的文件进行二进制的写操作
#         destination = open(os.path.join("E:\\upload", myFile.name), 'wb+')
#         for chunk in myFile.chunks():      # 分块写入文件
#             destination.write(chunk)
#         destination.close()
#         return HttpResponse("upload over!")
