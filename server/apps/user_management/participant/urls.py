from django.urls import path

app_name = "participant"

urlpatterns = [
    path("register/", register_participant, name="register_participant"),
]
