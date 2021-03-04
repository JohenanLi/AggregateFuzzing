from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render,HttpResponse,redirect 
# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'
