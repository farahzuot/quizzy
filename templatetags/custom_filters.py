from django import template

from server.apps.quiz.models import Option

register = template.Library()


@register.filter
def truncate_chars(value, max_length):
    if len(value) > max_length:
        return value[: max_length - 3] + "..."
    return value


@register.filter
def get_options(question):
    return Option.objects.filter(question=question)
