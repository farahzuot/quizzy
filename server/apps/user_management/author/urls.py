from django.urls import path

from server.apps.user_management.author.views import register_author

app_name = "author"

urlpatterns = [
    path("register/", register_author, name="register_author"),
]
