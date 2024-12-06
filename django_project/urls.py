
from django.urls import path
from Economation import views
from django.contrib import admin

urlpatterns = [
    path('', views.inicio, name='inicio'),  
]