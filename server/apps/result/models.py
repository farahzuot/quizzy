from django.db import models

from server.apps.main.models import BaseModel
from server.apps.quiz.models import Option, Question, Quiz
from server.apps.user_management.participant.models import Participant


class QuizResult(BaseModel):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="results")
    participant = models.ForeignKey(
        Participant, on_delete=models.CASCADE, related_name="quiz_results"
    )
    score = models.PositiveIntegerField(null=True, blank=True)
    passed = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"{self.participant.user.username}'s result for {self.quiz.title}"


class UserAnswer(BaseModel):
    participant = models.ForeignKey(
        Participant, on_delete=models.CASCADE, related_name="quiz_answers"
    )
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="user_answers"
    )

    tf_answer = models.BooleanField(null=True, blank=True)
    result = models.ForeignKey(
        QuizResult, on_delete=models.CASCADE, related_name="answers"
    )

    def __init__(self, *args, **kwargs):
        question_instance = kwargs.pop("question_instance", None)
        super(UserAnswer, self).__init__(*args, **kwargs)
        if question_instance:
            self.fields["answer"].queryset = Option.objects.filter(
                question=question_instance
            )

    def __str__(self):
        return f"{self.participant.user.username}'s answer to {self.question.question_text}"


class UserAnswerOption(BaseModel):
    user_answer = models.ForeignKey(
        UserAnswer, on_delete=models.CASCADE, related_name="correct_options"
    )
    option = models.ForeignKey(
        Option,
        on_delete=models.CASCADE,
        related_name="user_answer_options",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.id}"
