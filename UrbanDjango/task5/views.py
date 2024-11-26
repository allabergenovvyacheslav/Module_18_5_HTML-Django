from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.

# Пробный код регистрации

# def registration_page(request):
#     return render(request, 'registration_page.html')
#
#
# def postuser(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     age = request.POST.get('age', 1)
#     return HttpResponse(f'<h2>'
#                         f'Ваш логин: {username}, '
#                         f'<p>Ваш пароль: {password},</p> '
#                         f'<p>Ваш возраст: {age}</p>'
#                         f'</h2>')


def sign_up_by_html(request):
    users = ['Nikita', 'Tatiana', 'Ekaterina', 'Vladimir']
    info = {}
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age', 1)
        context = {'info': info}

        if username not in users and password == repeat_password and int(age) > 18:
            return HttpResponse(f'Приветствую, {username}!')
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            return render(request, 'registration_page.html', context)
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', context)
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, 'registration_page.html', context)
    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    users = ['Nikita', 'Tatiana', 'Ekaterina', 'Vladimir']
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age', 1)
            context = {'info': info, 'form': form}

            if username not in users and password == repeat_password and int(age) > 18:
                return HttpResponse(f'Приветствую, {username}!')
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', context)
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', context)
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', context)

        else:
            form = UserRegister()
        return render(request, 'registration_page.html', {'form': form})
