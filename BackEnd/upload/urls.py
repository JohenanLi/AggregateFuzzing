from django.urls import path, include
from .views import *
urlpatterns = [
    path('index/', IndexView.as_view(), name='index')
]
