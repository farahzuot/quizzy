from django.urls import path

from server.apps.quiz.views import CreateQuiz, ListQuizView, create_quiz_settings, add_question

app_name = 'quiz'

urlpatterns = [
    path('', ListQuizView.as_view(template_name='quiz/quiz_list.html'), name='List_quiz'),
    # path('create/', CreateQuiz.as_view(template_name='quiz/quiz_create.html'), name='create_quiz'),

    path('create/', create_quiz_settings, name='create_quiz'),
    path('add-question/', add_question, name='add_question'),
]
