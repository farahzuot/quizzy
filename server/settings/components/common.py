"""
Django settings for server project.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their config, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from typing import Dict, List, Tuple, Union

from django.utils.translation import gettext_lazy as _

from server.settings.components import BASE_DIR, config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = config('DJANGO_SECRET_KEY')

# Application definition:

INSTALLED_APPS: Tuple[str, ...] = (
    # Your apps go here:
    'server.apps.main',
    'server.apps.user_management.author',
    'server.apps.user_management.participant',
    'server.apps.user_management.user',
    'server.apps.quiz',
    'server.apps.result',

    # Default django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django-admin:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Security:
    # 'axes'

    # Health checks:
    # You may want to enable other checks as well,
    # see: https://github.com/KristianOellegaard/django-health-check
    'health_check',
    'health_check.db',
    'health_check.cache',
    'health_check.storage',
)

MIDDLEWARE: Tuple[str, ...] = (
    # Logging:
    'server.settings.components.logging.LoggingContextVarsMiddleware',

    # Content Security Policy:
    # 'csp.middleware.CSPMiddleware',

    # Django:
    'django.middleware.security.SecurityMiddleware',
    # django-permissions-policy
    'django_permissions_policy.PermissionsPolicyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Axes:
    # 'axes.middleware.AxesMiddleware',

    # Django HTTP Referrer Policy:
    'django_http_referrer_policy.middleware.ReferrerPolicyMiddleware',
)

ROOT_URLCONF = 'server.urls'

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': config('POSTGRES_DB'),
    #     'USER': config('POSTGRES_USER'),
    #     'PASSWORD': config('POSTGRES_PASSWORD'),
    #     'HOST': config('DJANGO_DATABASE_HOST'),
    #     'PORT': config('DJANGO_DATABASE_PORT', cast=int),
    #     'CONN_MAX_AGE': config('CONN_MAX_AGE', cast=int, default=60),
    #     'OPTIONS': {
    #         'connect_timeout': 10,
    #         'options': '-c statement_timeout=15000ms',
    #     },
    # },
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

# LANGUAGES = (
#     ('en', _('English')),
#     ('ru', _('Russian')),
# )

LOCALE_PATHS = [
    os.path.join(BASE_DIR, '_locale'),
]

USE_TZ = True
TIME_ZONE = 'UTC'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'assets/'

STATICFILES_DIRS = [
    BASE_DIR / 'assets',
    BASE_DIR / 'static',
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Templates
# https://docs.djangoproject.com/en/4.2/ref/templates/api

TEMPLATES = [{
    'APP_DIRS': True,
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, '_templates')],

    'OPTIONS': {
        'context_processors': [
            # Default template context processors:
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.contrib.messages.context_processors.messages',
            'django.template.context_processors.request',
        ],
        'libraries': {
            'theme': '_keenthemes.templatetags.theme',
            'custom_filters': 'templatetags.custom_filters',
        },
        'builtins': [
            'django.templatetags.static',
            '_keenthemes.templatetags.theme',
        ]
    },
}]


# Media files
# Media root dir is commonly changed in production
# (see development.py and production.py).
# https://docs.djangoproject.com/en/4.2/topics/files/

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')

# Django authentication system
# https://docs.djangoproject.com/en/4.2/topics/auth/

AUTHENTICATION_BACKENDS = (
    # 'axes.backends.AxesBackend',
    'django.contrib.auth.backends.ModelBackend',
)

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Security
# https://docs.djangoproject.com/en/4.2/topics/security/

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = 'DENY'

# https://github.com/DmytroLitvinov/django-http-referrer-policy
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
REFERRER_POLICY = 'same-origin'

# https://github.com/adamchainz/django-permissions-policy#setting
PERMISSIONS_POLICY: Dict[str, Union[str, List[str]]] = {}  # noqa: WPS234

# Timeouts
# https://docs.djangoproject.com/en/4.2/ref/settings/#std:setting-EMAIL_TIMEOUT

EMAIL_TIMEOUT = 5

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

######################
# Keenthemes Settings
######################

KT_THEME = 'metronic'

# Theme layout _templates directory

KT_THEME_LAYOUT_DIR = 'layout'

# Theme Mode
# Value: light | dark | system

KT_THEME_MODE_DEFAULT = 'light'
KT_THEME_MODE_SWITCH_ENABLED = True

# Theme Direction
# Value: ltr | rtl

KT_THEME_DIRECTION = 'ltr'

# Keenicons
# Value: duotone | outline | bold

KT_THEME_ICONS = 'duotone'

# Theme Assets

KT_THEME_ASSETS = {
    "favicon": "media/logos/favicon.ico",
    "fonts": [
        'https://fonts.googleapis.com/css?family=Inter:300,400,500,600,700',
    ],
    "css": [
        "plugins/global/plugins.bundle.css",
        "css/style.bundle.css"
    ],
    "js": [
        "plugins/global/plugins.bundle.js",
        "js/scripts.bundle.js",
    ]
}

# Theme Vendors

KT_THEME_VENDORS = {
    "datatables": {
        "css": [
            "plugins/custom/datatables/datatables.bundle.css"
        ],
        "js": [
            "plugins/custom/datatables/datatables.bundle.js"
        ]
    },
    "formrepeater": {
        "js": [
            "plugins/custom/formrepeater/formrepeater.bundle.js"
        ]
    },
    "fullcalendar": {
        "css": [
            "plugins/custom/fullcalendar/fullcalendar.bundle.css"
        ],
        "js": [
            "plugins/custom/fullcalendar/fullcalendar.bundle.js"
        ]
    },
    "flotcharts": {
        "js": [
            "plugins/custom/flotcharts/flotcharts.bundle.js"
        ]
    },
    "google-jsapi": {
        "js": [
            "//www.google.com/jsapi"
        ]
    },
    "tinymce": {
        "js": [
            "plugins/custom/tinymce/tinymce.bundle.js"
        ]
    },
    "ckeditor-classic": {
        "js": [
            "plugins/custom/ckeditor/ckeditor-classic.bundle.js"
        ]
    },
    "ckeditor-inline": {
        "js": [
            "plugins/custom/ckeditor/ckeditor-inline.bundle.js"
        ]
    },
    "ckeditor-balloon": {
        "js": [
            "plugins/custom/ckeditor/ckeditor-balloon.bundle.js"
        ]
    },
    "ckeditor-balloon-block": {
        "js": [
            "plugins/custom/ckeditor/ckeditor-balloon-block.bundle.js"
        ]
    },
    "ckeditor-document": {
        "js": [
            "plugins/custom/ckeditor/ckeditor-document.bundle.js"
        ]
    },
    "draggable": {
        "js": [
            "plugins/custom/draggable/draggable.bundle.js"
        ]
    },
    "fslightbox": {
        "js": [
            "plugins/custom/fslightbox/fslightbox.bundle.js"
        ]
    },
    "jkanban": {
        "css": [
            "plugins/custom/jkanban/jkanban.bundle.css"
        ],
        "js": [
            "plugins/custom/jkanban/jkanban.bundle.js"
        ]
    },
    "typedjs": {
        "js": [
            "plugins/custom/typedjs/typedjs.bundle.js"
        ]
    },
    "cookiealert": {
        "css": [
            "plugins/custom/cookiealert/cookiealert.bundle.css"
        ],
        "js": [
            "plugins/custom/cookiealert/cookiealert.bundle.js"
        ]
    },
    "cropper": {
        "css": [
            "plugins/custom/cropper/cropper.bundle.css"
        ],
        "js": [
            "plugins/custom/cropper/cropper.bundle.js"
        ]
    },
    "vis-timeline": {
        "css": [
            "plugins/custom/vis-timeline/vis-timeline.bundle.css"
        ],
        "js": [
            "plugins/custom/vis-timeline/vis-timeline.bundle.js"
        ]
    },
    "jstree": {
        "css": [
            "plugins/custom/jstree/jstree.bundle.css"
        ],
        "js": [
            "plugins/custom/jstree/jstree.bundle.js"
        ]
    },
    "prismjs": {
        "css": [
            "plugins/custom/prismjs/prismjs.bundle.css"
        ],
        "js": [
            "plugins/custom/prismjs/prismjs.bundle.js"
        ]
    },
    "leaflet": {
        "css": [
            "plugins/custom/leaflet/leaflet.bundle.css"
        ],
        "js": [
            "plugins/custom/leaflet/leaflet.bundle.js"
        ]
    },
    "amcharts": {
        "js": [
            "https://cdn.amcharts.com/lib/5/index.js",
            "https://cdn.amcharts.com/lib/5/xy.js",
            "https://cdn.amcharts.com/lib/5/percent.js",
            "https://cdn.amcharts.com/lib/5/radar.js",
            "https://cdn.amcharts.com/lib/5/themes/Animated.js"
        ]
    },
    "amcharts-maps": {
        "js": [
            "https://cdn.amcharts.com/lib/5/index.js",
            "https://cdn.amcharts.com/lib/5/map.js",
            "https://cdn.amcharts.com/lib/5/geodata/worldLow.js",
            "https://cdn.amcharts.com/lib/5/geodata/continentsLow.js",
            "https://cdn.amcharts.com/lib/5/geodata/usaLow.js",
            "https://cdn.amcharts.com/lib/5/geodata/worldTimeZonesLow.js",
            "https://cdn.amcharts.com/lib/5/geodata/worldTimeZoneAreasLow.js",
            "https://cdn.amcharts.com/lib/5/themes/Animated.js"
        ]
    },
    "amcharts-stock": {
        "js": [
            "https://cdn.amcharts.com/lib/5/index.js",
            "https://cdn.amcharts.com/lib/5/xy.js",
            "https://cdn.amcharts.com/lib/5/themes/Animated.js"
        ]
    },
    "bootstrap-select": {
        "css": [
            "plugins/custom/bootstrap-select/bootstrap-select.bundle.css"
        ],
        "js": [
            "plugins/custom/bootstrap-select/bootstrap-select.bundle.js"
        ]
    }
}
