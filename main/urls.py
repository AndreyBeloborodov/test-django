from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexHome, name='home')
]