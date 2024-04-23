from django.urls import path, re_path
from articles import views


urlpatterns = [
    re_path(r"^$|^article/$", views.ArticleListView.as_view(), name="article_list"),
    path("article/<int:pk>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("article/tags=<str:tags>/", views.ArticleTagsListView.as_view(), name="article_create"),
    path("article/create/", views.ArticleCreateView.as_view(), name="article_create"),
]
