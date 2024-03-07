# forms.py
from django import forms
from django.forms import formset_factory

from server.apps.quiz.models import Quiz, Question, Option


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'passing_score', 'difficulty_level', 'time_limit']


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['option_text', 'is_correct']


OptionFormSet = formset_factory(OptionForm, extra=2)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_type', 'question_text', 'marks', 'tf_correct_answer']

        widgets = {
            'question_type': forms.RadioSelect(choices=[('True/False', 'tf'), ('Multiple Choice', 'mc')]),

            'tf_correct_answer': forms.RadioSelect(choices=[(True, 'True'), (False, 'False')]),
        }
