from django.urls import path

from server.apps.user_management.user.views import (
    login_view,
    logout_view,
    register,
)

app_name = "user"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
