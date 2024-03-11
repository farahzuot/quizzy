from django.contrib.auth.models import User
from django.db import models

from server.apps.main.models import BaseModel


# Create your models here.
class BaseUser(BaseModel):
    """Quiz Participant model."""

    phone_number = models.CharField(
        max_length=100,
        blank=True,
    )
    nationality = models.CharField(
        max_length=100,
        blank=True,
    )
    date_of_birth = models.DateField(auto_now=False, blank=True, null=True)
    active = "active"
    inactive = "inactive"
    status_select = [
        (active, "active"),
        (inactive, "inactive"),
    ]
    status = models.CharField(
        max_length=13,
        choices=status_select,
        default=inactive,
    )

    class Meta:
        abstract = True
