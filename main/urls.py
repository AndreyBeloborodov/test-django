from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexHome, name='home'),
    path('/good', views.indexGood, name = 'good'),
    path('/bad', views.indexBad, name = 'bad')
]