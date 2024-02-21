from django.db import models

from server.apps.main.models import BaseModel
from server.apps.user_management.author.models import Author


class Quiz(BaseModel):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='quiz_author')
    title = models.CharField(max_length=100)
    description = models.TextField()
    passing_score = models.PositiveIntegerField(blank=True, null=True)
    difficulty_level = models.CharField(max_length=100, blank=True, null=True)
    time_limit = models.CharField(max_length=100, blank=True, null=True)

    class Meta(object):
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.title


class Question(BaseModel):
    MULTIPLE_CHOICE = 'mc'
    TRUE_FALSE = 'tf'

    QUESTION_TYPES = [
        (MULTIPLE_CHOICE, 'Multiple Choice'),
        (TRUE_FALSE, 'True/False'),
    ]

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPES)
    question_text = models.TextField()
    marks = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.question_text


class Option(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.option_text}'s answer to {self.question.question_text}"
