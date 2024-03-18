from django.urls import path

from server.apps.result.views import take_quiz, quiz_result

app_name = "result"

urlpatterns = [
    path('quiz/<str:quiz_id>/', take_quiz, name='take_quiz'),
    path('quiz/result/<int:quiz_result_id>/', quiz_result, name='quiz_result'),
]
