from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]
# Create your views here.
