#Creates URL for contact

from django.urls import path, include
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index')
]
