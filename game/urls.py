from django.urls import path
from django.shortcuts import render, redirect
from . import views
app_name = "game"
urlpatterns = [
    path("level/", views.levels, name="levels"),
    path("level/<int:level_id>", views.level_detail, name="level_detail"),
    path("level2/", views.level_detail2, name="level_detail2"),
    # path("search/", views.post_search, name="post_search"),
    # path("model/", views.model_predict, name="model_predict"),
]