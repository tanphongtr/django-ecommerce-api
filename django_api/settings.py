"""
Django settings for django_api project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vn5iga)cc=i6n$w&zz45u)$@(#c&oal%77w77b8y0b)bs1o#t6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Application startapp

INSTALLED_APPS += [
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',  # swagger
    'app',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE += [
    # da ngon ngu
    'django.middleware.locale.LocaleMiddleware',
    'drf_yasg.middleware.SwaggerExceptionMiddleware',
    # DataFlair #Caching Middleware

    # Cache
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'django_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MARIADB_DATABASE', 'django_api'),
        'USER': os.getenv('MARIADB_ROOT_USER', 'root'),
        'PASSWORD': os.getenv('MARIADB_ROOT_PASSWORD', '123456'),
        # Or an IP Address that your DB is hosted on, 0.0.0.0 in docker linux
        #
        'HOST': os.getenv('MARIADB_CONTAINER_NAME', 'localhost'),
        'PORT': os.getenv('MARIADB_PORT', '3366'),
    },

    'other': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_api2',
        'USER': 'root',
        'PASSWORD': '123456',
        # Or an IP Address that your DB is hosted on, 0.0.0.0 in docker linux
        'HOST': 'localhost',
        'PORT': '3366',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "files")
STATIC_ROOT = "var/www/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'django_api', 'static'),
]


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_AUTO_FIELD = 'app.models.UnsignedAutoField'


# Rest Framework
REST_FRAMEWORK = {

    # API version
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    # 'DEFAULT_VERSION': 'v1', # comment tren swagger se hien nhieu phien ban
    # 'ALLOWED_VERSIONS': ('v1', 'v2'),

    # Unix timestamp, only on Docker/Linux
    # 'DATETIME_FORMAT': '%s.%f',


    # 'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S.%fZ',

    # Timestamp for Js
    # 'DATETIME_FORMAT': '%s000.%f',

    # 'DATE_FORMAT': '%s000.%f',

    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'EXCEPTION_HANDLER': 'app.utils.custom_exception_handler',

    # 'EXCEPTION_HANDLER': 'django_api.ultils.exception.custom_exception_handler', # Thông báo lỗi

    # https://www.django-rest-framework.org/api-guide/metadata/
    # 'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
}

SWAGGER_SETTINGS = {
    # 'USE_SESSION_AUTH': False,
    # 'SECURITY_DEFINITIONS': {
    #     'basic': {
    #         'type': 'basic'
    #     },
    #     'api_key': {
    #         'type': 'apiKey',
    #         'in': 'header',
    #         'name': 'Authorization'
    #     }
    # },
    # 'APIS_SORTER': 'alpha',
    'SUPPORTED_SUBMIT_METHODS': ['get', 'post', 'put', 'delete', 'patch'],
    'OPERATIONS_SORTER': 'alpha',
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },

    # Hidden model in swagger docs
    'DEFAULT_FIELD_INSPECTORS': [
        'drf_yasg.inspectors.CamelCaseJSONFilter',
        'drf_yasg.inspectors.InlineSerializerInspector',
        'drf_yasg.inspectors.RelatedFieldInspector',
        'drf_yasg.inspectors.ChoiceFieldInspector',
        'drf_yasg.inspectors.FileFieldInspector',
        'drf_yasg.inspectors.DictFieldInspector',
        'drf_yasg.inspectors.SimpleFieldInspector',
        'drf_yasg.inspectors.StringDefaultFieldInspector',
    ],

}

LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
    ('vi-vn', _('Vietnamese')),
]

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#         'TIMEOUT': 604800
#     }
# }


# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://" + os.getenv('REDIS_CONTAINER_NAME', '127.0.0.1') + ":6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "SOCKET_CONNECT_TIMEOUT": 5,  # seconds
#             "SOCKET_TIMEOUT": 5,  # seconds
#         },
#         "KEY_PREFIX": "example",
#         "TIMEOUT": 5,
#         "TTL": 5,
#     }
# }

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


# Locale
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]


def custom404(request, exception=None):
    return JsonResponse({
        'status_code': 404,
        'error': 'The resource was not found'
    })


handler404 = custom404

# AUTH_USER_MODEL = 'app.User'


# print( os.environ )


# Send mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tanphongtr@gmail.com'
EMAIL_HOST_PASSWORD = 'ucnditvoiovkzawu'  # past the key or password app here
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'default from email'

# DEFAULT_AUTO_FIELD Default: 'django.db.models.AutoField'
# DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'







































"""
Django settings for django_test project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.utils.translation import gettext as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-k1jwx3_=j%4_q%nj1l_9v(j9a#*kf64i!&3_h3+l8)fj*em4j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


REDOC_SETTINGS = {
    'LAZY_RENDERING': False,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'drf_yasg.middleware.SwaggerExceptionMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]




# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

MIDDLEWARE_CLASSES = [
    'django.middleware.locale.LocaleMiddleware'
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# LANGUAGES = [
#     ('de', _('German')),
#     ('en', _('English')),
# ]

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/files/'
MEDIA_ROOT = os.path.join(BASE_DIR, "files")
STATIC_ROOT = "var/www/static/"
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'django_test', 'static'),
]

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

# print( os.environ.get('') )