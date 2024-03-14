from django.contrib.auth.mixins import UserPassesTestMixin


class AuthorPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and hasattr(self.request.user, 'author')
