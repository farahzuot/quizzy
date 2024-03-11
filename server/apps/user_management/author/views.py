from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from _keenthemes import KTLayout
from server.apps.user_management.author.forms import RegisterAuthorForm


def register_author(request):
    user_id = request.session.get("user_id")
    if request.method == "POST":
        form = RegisterAuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = get_object_or_404(User, id=user_id)
            author.save()
            return redirect("user:login")
    else:
        form = RegisterAuthorForm()
    context = {"form": form}
    context = KTLayout.init(context)
    return render(request, "accounts/register_author.html", context)
