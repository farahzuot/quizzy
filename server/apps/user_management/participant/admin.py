from django.contrib import admin

from server.apps.user_management.participant.models import Participant


# Register your models here.
class ParticipantAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')


admin.site.register(Participant, ParticipantAdmin)
