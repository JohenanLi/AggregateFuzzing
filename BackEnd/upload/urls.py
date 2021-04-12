from django.urls import path, include
from .views import sourceCode,sourceProgram,uploadCode,uploadInputFile
urlpatterns = [
    path('sourceCode/',sourceCode),
    path('sourceProgram/',sourceProgram),
    path("uploadCode/",uploadCode),
    path("uploadInputFile/",uploadInputFile)
]
