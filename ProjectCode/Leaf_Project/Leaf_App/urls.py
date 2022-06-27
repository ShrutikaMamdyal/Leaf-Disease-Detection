from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home,name="Home"),
    path('result/',views.Result,name="Result"),
    path('help/',views.Help,name="Help")
]