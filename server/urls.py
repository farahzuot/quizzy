"""
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.admindocs import urls as admindocs_urls
from django.urls import include, path
from django.views.generic import TemplateView
from health_check import urls as health_urls

from server.apps.main import urls as main_urls
from server.apps.main.views import MainView
from server.apps.quiz import urls as quiz_urls
from server.apps.user_management.author import urls as author_urls
from server.apps.user_management.participant import urls as participant_urls
from server.apps.user_management.user import urls as user_urls

admin.autodiscover()

urlpatterns = [
    # Apps:
    path("main/", include(main_urls, namespace="main")),
    path("quiz/", include(quiz_urls, namespace="quiz")),
    path("accounts/", include(user_urls, namespace="user")),
    path("author/", include(author_urls, namespace="author")),
    path("participant/", include(participant_urls, namespace="participant")),
    # Health checks:
    path("health/", include(health_urls)),
    # django-admin:
    path("admin/doc/", include(admindocs_urls)),
    path("admin/", admin.site.urls),
    # Text and xml static files:
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="txt/robots.txt",
            content_type="text/plain",
        ),
    ),
    path(
        "humans.txt",
        TemplateView.as_view(
            template_name="txt/humans.txt",
            content_type="text/plain",
        ),
    ),
    # It is a good practice to have explicit index view:
    path("", MainView.as_view(template_name="main/index.html"), name="home"),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar  # noqa: WPS433
    from django.conf.urls.static import static  # noqa: WPS433

    urlpatterns = [
        # URLs specific only to django-debug-toolbar:
        path("__debug__/", include(debug_toolbar.urls)),
        *urlpatterns,
        # Serving media files in development only:
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    ]
