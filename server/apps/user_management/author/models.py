from typing import final

from django.contrib.auth.models import User
from django.db import models

from server.apps.user_management.user.models import BaseUser


# Create your models here.

@final
class Author(BaseUser):
    """ Quiz author model. """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="author",
    )
    class Meta(object):
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
