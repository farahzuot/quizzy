from django.urls import path

from server.apps.quiz.views import (
    ListQuizView,
    AddQuestion,
    CreateQuizSettings,
)

app_name = "quiz"

urlpatterns = [
    path(
        "", ListQuizView.as_view(template_name="quiz/quiz_list.html"), name="list_quiz"
    ),
    path("create/", CreateQuizSettings.as_view(), name="create_quiz"),
    path("add-question/", AddQuestion.as_view(), name="add_question"),
]
