from django.urls import path
from django.shortcuts import render, redirect
from . import views
app_name = "helpus"
urlpatterns = [
    path("register", views.register_contribute, name="register_contribute"),
    path("", views.contribute, name="contribute"),
]