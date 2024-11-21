
from django.urls import path
from economation import views
from django.contrib import admin

urlpatterns = [
    path('', views.inicio, name='inicio'),  
]