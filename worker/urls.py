from django.urls import path,include
from django.shortcuts import render, redirect
from . import views

urlpatterns = [
    path('', views.SearchBarcode, name='search-barcode'),
    path('drawmap/', views.drawmap),
]