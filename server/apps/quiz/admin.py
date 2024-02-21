from django.contrib import admin
from server.apps.quiz.models import Quiz, Question, Option

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
