from django.urls import path,include
from django.shortcuts import render, redirect
from . import views


urlpatterns = [
    path('', views.searchbook, name = "search-book"),
#   path('', views.searchedbooklist, name ="searched-booklist"),
    path('drawmap/<int:id>', views.drawmap, name ="drawing-map"),
]