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
    production = ['Parquet flooring',
                  'Solid wood board',
                  'large format parquet']
    text_buy = 'Choose'
    text_back = 'Go back'
    context = {
        'title': title,
        'production': production,
        'text_buy': text_buy,
        'text_back': text_back
    }
    return render(request, 'products.html', context)


def cart(request):
    title = 'Your choice of products:'
    your_choice = 'Sorry, your cart is empty'
    text_back = 'Go back'
    context = {
        "title": title,
        'your_choice': your_choice,
        'text_back': text_back
    }
    return render(request, 'cart.html', context)
