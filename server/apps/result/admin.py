from django.contrib import admin

from server.apps.result.models import QuizResult, UserAnswer, UserAnswerOption


# Register your models here.
class QuizResultAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).select_related("participant__user", "quiz")


class UserAnswerAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related("participant__user", "question")
        )


admin.site.register(QuizResult, QuizResultAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)
admin.site.register(UserAnswerOption)
