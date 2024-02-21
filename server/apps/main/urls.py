from django.urls import path

from server.apps.main.views import MainView

app_name = 'main'

urlpatterns = [
    path('hello/', MainView.as_view(template_name='main/index.html'), name='hello'),
]
