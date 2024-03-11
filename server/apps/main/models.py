import textwrap
import uuid
from typing import Final, final

from django.db import models

#: That's how constants should be defined.
_POST_TITLE_MAX_LENGTH: Final = 80


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
