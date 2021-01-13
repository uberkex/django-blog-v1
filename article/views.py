from django.shortcuts import render, get_object_or_404
from .models import Article, Category


# Create your views here.

# Deneme View
def article_list(request):
    mesaj = "Burası Article List Sayfası"

    context = {
        'msg': mesaj,
    }

    return render(request, 'deneme.html', context)


# Article Home View
def article_home(request):
    baslik = "Django Makaleleri"
    articles = Article.objects.filter(status=1)

    context = {
        'title': baslik,
        'articles': articles,
    }

    return render(request, 'index.html', context)


# Article Detail View
def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    # article = get_object_or_404(Article, slug=slug)

    context = {
        'article': article,
    }

    return render(request, 'blog-post.html', context)


# Category List View
def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }

    return render(request, 'category_list.html', context)


# Category Detail View
def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    category_articles = Article.objects.filter(category=category)

    context = {
        'category': category,
        'category_articles': category_articles,
    }

    return render(request, 'category_detail.html', context)
