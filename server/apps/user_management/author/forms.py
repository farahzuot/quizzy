from django import forms

from server.apps.user_management.author.models import Author


class RegisterAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["phone_number", "nationality", "date_of_birth"]
