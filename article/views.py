from django.shortcuts import render


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

    context = {
        'title': baslik,
    }

    return render(request, 'index.html', context)
