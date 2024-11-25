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
    text_prod = 'Company products'
    production = ['Parquet flooring 70mm',
                  'Solid wood board 120mm',
                  'large format parquet 90mm']
    text_buy = 'Choose'
    text_back = 'Go back'
    context = {
        'text_prod': text_prod,
        'production': production,
        'text_buy': text_buy,
        'text_back': text_back,
    }
    return render(request, 'products.html', context)


def cart(request):
    text_cart = 'Your choice of products:'
    your_choice = 'Sorry, your cart is empty'
    text_back = 'Go back'
    context = {
        "text_cart": text_cart,
        'your_choice': your_choice,
        'text_back': text_back,
    }
    return render(request, 'cart.html', context)
