from django.urls import path
from . import views
from .views import PostListView


app_name = "blog"
urlpatterns = [
    # post views
    path("", views.PostListView.as_view(), name="post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path("<int:post_id>/share/", views.post_share, name="post_share"),
    path("search/", views.post_search, name="post_search"),
    path("model/predict", views.model_predict, name="model_predict"),
]
