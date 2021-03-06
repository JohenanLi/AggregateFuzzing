from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render,HttpResponse,redirect,render
from django.views.generic.base import TemplateView, View 
# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'

def sourceCode(request):
    if request.method == 'GET':
        return render(request,'sourceCode/sourceCode.html')
    elif request.method == 'POST':
        source = request.POST.GET('sourceCode')
        languangeType = request.POST.GET('languageType')
        parameter = request.POST.GET('parameter')
        ##调用接口传数据
        return render(request,'sourceCode/wait.html')

def sourceProgram(request):
    if request.method == 'GET':
        return render(request,'sourceProgram/sourceProgram.html')
    elif request.method == 'POST':
        pass

