from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from _keenthemes import KTLayout
from server.apps.user_management.user.forms import (
    LoginForm,
    RegisterAuthorForm,
    RegisterForm,
    RegisterParticipantForm,
)

# Create your views here.


def register(request):
    account_type = request.GET.get("account_type")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session["user_id"] = str(user.id)
            if account_type == "author":
                return redirect("author:register_author")
            elif account_type == "participant":
                return redirect("participant:register_participant")
    else:
        form = RegisterForm()
    context = {"form": form}
    context = KTLayout.init(context)
    return render(request, "accounts/register.html", context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    context = {"form": form}
    context = KTLayout.init(context)
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("user:login")
