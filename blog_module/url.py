from django.urls import path
from . import views

app_name = 'blog_module'
urlpatterns = [
    path("article_list", views.ArticleListView.as_view(), name="article_list"),
    path("article_detail/<slug:slug>", views.ArticleDetailView.as_view(), name="article_detail"),
]