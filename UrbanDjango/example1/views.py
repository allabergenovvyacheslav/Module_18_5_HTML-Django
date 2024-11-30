from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Category
from .forms import ContactForm, FeedBackForm

# Create your views here.


def home(request):
    categories = Category.objects.all()
    return render(request,
                  'home.html',
                  {'categories': categories})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено')
    else:
        form = ContactForm()
    return render(request,
                  'contact.html',
                  {'form': form})


def feedback_view(request):
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,
                          'feedback_success.html')
    else:
        form = FeedBackForm()
    return render(request,
                  'feedback_form.html',
                  {'form': form})


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
