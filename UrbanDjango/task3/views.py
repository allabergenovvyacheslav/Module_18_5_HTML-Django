from django.shortcuts import render


# Create your views here.


def platform(request):
    title = 'World of oak flooring'
    text = 'Home page'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'platform.html', context)


def products(request):
    title = 'Company products'
    text_1 = 'Parquet flooring'
    text_2 = 'Solid wood board'
    text_3 = 'large format parquet'
    text_buy = 'Choose'
    text_back = 'Go back'
    context = {
        'title': title,
        'text_1': text_1,
        'text_2': text_2,
        'text_3': text_3,
        'text_buy': text_buy,
        'text_back': text_back
    }
    return render(request, 'products.html', context)


def cart(request):
    title = 'Your choice of products:'
    text_1 = 'Good! Parquet flooring'
    text_2 = 'Wherry good! Solid wood board'
    text_3 = 'Excellent choice! Large format parquet'
    text_back = 'Go back'
    context = {
        "title": title,
        'text_1': text_1,
        'text_2': text_2,
        'text_3': text_3,
        'text_back': text_back
    }
    return render(request, 'cart.html', context)
