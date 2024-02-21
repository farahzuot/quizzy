from django.contrib import admin

from server.apps.user_management.author.models import Author


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')


admin.site.register(Author, AuthorAdmin)
