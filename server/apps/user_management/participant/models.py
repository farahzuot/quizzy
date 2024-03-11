from typing import final

from django.contrib.auth.models import User
from django.db import models

from server.apps.user_management.user.models import BaseUser

# Create your models here.


@final
class Participant(BaseUser):
    """Quiz Participant model."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="participant",
    )

    class Meta(object):
        verbose_name = "Participant"
        verbose_name_plural = "Participants"

    def __str__(self) -> str:
        """Representation method."""
        return self.user.username if self.user else str(self.id)
