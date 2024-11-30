from django.shortcuts import render

from .models import Product

# Create your views here.


def product_list(request):
    products = Product.objects.all()
    return render(request,
                  'product_list.html',
                  {'products': products})


def phones_list(request):
    products = Product.objects.filter(category__name="Телефоны")
    return render(request,
                  'phones_list.html',
                  {'products': products})
