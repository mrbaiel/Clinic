from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from users.forms import User,UserLoginForm, UserRegistrationForm
from django.urls import reverse
# Create your views here.


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)  #достаем пользователя из бд и проверяем

            if user:
                auth.login(request , user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST': # если у нвс POST запрос то создаем форму
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()  # сохраняем данные
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {'title':"Kasiet-Профиль"}
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))