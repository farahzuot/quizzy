from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from _keenthemes import KTLayout
from server.apps.user_management.participant.forms import (
    RegisterParticipantForm,
)

# Create your views here.


def register_participant(request):
    user_id = request.session.get("user_id")
    if request.method == "POST":
        form = RegisterParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.user = get_object_or_404(User, id=user_id)
            participant.save()
            return redirect("user:login")
    else:
        form = RegisterParticipantForm()
    context = {"form": form}
    context = KTLayout.init(context)
    return render(request, "accounts/register_participant.html", context)
