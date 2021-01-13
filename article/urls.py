from django.urls import path
from . import views

# from article.views import article_list

app_name = "article"

urlpatterns = [
    path('', views.article_home, name="article_home"),
    path('<slug:slug>/', views.article_detail, name="article_detail"),
    path('articles/', views.article_list, name="article_list"),

    path('categories/list/', views.category_list, name="category_list"),
    path('category/<slug:slug>/', views.category_detail, name="category_detail"),

]
