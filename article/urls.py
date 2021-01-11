from django.urls import path
from . import views
# from article.views import article_list

app_name = "article"

urlpatterns = [
    path('', views.article_home(), name="article_home"),
    path('articles/', views.article_list, name="article_list"),

]