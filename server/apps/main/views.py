from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from _keenthemes.__init__ import KTLayout
from _keenthemes.libs.theme import KTTheme
from server.apps.quiz.models import Quiz


class MainView(ListView):
    model = Quiz
    template_name = "quiz/quiz_list.html"
    context_object_name = "quizzes"

    def get_queryset(self):
        return Quiz.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = KTLayout.init(context)
        KTTheme.addJavascriptFile("js/home.js")
        KTTheme.addCssFile("css/style.css")
        return context
