from django.shortcuts import render
from .forms import UserRegister

users = ['Tom', 'James', 'Oleg', 'Olga']


def sign_up_by_django(request):
    return process_registration(request)


def sign_up_by_html(request):
    return process_registration(request)


def process_registration(request):
    info = {}
    if request.method=='POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password!=repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                info['success_message'] = f'Вы зарегистрированы, {username}!'
        else:
            info['error'] = 'Пожалуйста, исправьте ошибки в форме.'
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'registration_page.html', info)