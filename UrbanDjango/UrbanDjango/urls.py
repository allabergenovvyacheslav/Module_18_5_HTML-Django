"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from task2.views import *
# from task3.views import *
# from task4.views import platform, products, cart
# from task5 import views
from example1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('class/', ClassTemplate.as_view()),
    # path('func/', func_template),
    # path('', platform),
    # path('platform/products/', products),
    # path('platform/cart/', cart),
    # path("registration_page/", views.registration_page),
    # path("postuser/", views.postuser),
    # path("", views.sign_up_by_html),
    # path("django_sign_up/", views.sign_up_by_django),
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('phones/', views.phones_list, name='phones_list'),
    path('contact/', views.contact_view, name='contact'),
    path('feedback/', views.feedback_view, name='feedback_form'),
]
