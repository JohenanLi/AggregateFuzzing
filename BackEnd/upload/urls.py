from django.urls import path, include
from .views import *
urlpatterns = [
    path('sourceCode/',sourceCode),
    path('sourceProgram/',sourceProgram),
    path("formdataTest/",formdataTest)
]
