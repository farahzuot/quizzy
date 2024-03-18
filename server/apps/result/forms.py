from django import forms

from server.apps.result.models import UserAnswer


class UserAnswerForm(forms.ModelForm):
    class Meta:
        model = UserAnswer
        fields = ('tf_answer',)
