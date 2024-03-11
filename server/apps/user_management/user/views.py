from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from _keenthemes import KTLayout
from server.apps.user_management.user.forms import RegisterForm, LoginForm


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = RegisterForm()
    context = {'form': form}
    context = KTLayout.init(context)
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    context = {'form': form}
    context = KTLayout.init(context)
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('user:login')
