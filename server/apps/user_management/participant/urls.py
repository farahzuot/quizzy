from django.urls import path

from server.apps.user_management.participant.views import register_participant

app_name = "participant"

urlpatterns = [
    path("register/", register_participant, name="register_participant"),
]
