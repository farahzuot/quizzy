from django import forms

from server.apps.user_management.participant.models import Participant


class RegisterParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ["phone_number", "nationality", "date_of_birth"]
