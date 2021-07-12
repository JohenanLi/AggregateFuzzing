from django.urls import path, include
from .views import sourceCode,sourceProgram,uploadCode,uploadInputFile,AvailList
urlpatterns = [
    path('sourceCode/',sourceCode),
    path('sourceProgram/',sourceProgram),
    path("uploadCode/",uploadCode),
    path("uploadInputFile/",uploadInputFile),
    path("availList/",AvailList.as_view())
]
