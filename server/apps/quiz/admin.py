from django.contrib import admin

from server.apps.quiz.models import Option, Question, Quiz

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
