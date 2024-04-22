from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from _keenthemes import KTLayout
from server.apps.user_management.author.forms import RegisterAuthorForm
from server.apps.user_management.participant.forms import RegisterParticipantForm
from server.apps.user_management.user.forms import (
    LoginForm,
    RegisterForm,
)


# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            participant_form = RegisterParticipantForm(request.POST)
            author_form = RegisterAuthorForm(request.POST)
            if author_form.is_valid():
                author_form = RegisterAuthorForm(request.POST)
                author = author_form.save(commit=False)
                author.user = get_object_or_404(User, id=user.id)
                author.save()
                participant = participant_form.save(commit=False)
                participant.user = get_object_or_404(User, id=user.id)
                participant.save()
                author.save()
                return redirect("user:login")
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
