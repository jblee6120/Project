from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.select, name="first_page"),
]