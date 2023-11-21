from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from products.models import ProductCategory, Product


# Create your views here.
def index(request):
    context = {
        "title": "Kasiet",
    }
    return render(request, 'products/index.html')


def products(request):
    context = {
        "title": "Каталог",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Упс, страница не найдена =(</h1>")
