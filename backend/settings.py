"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'knox',
    'fcm_django',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS Requests
CORS_ORIGIN_ALLOW_ALL = True

# Uploads
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads/")
MEDIA_URL = "/media/"

ROOT_URLCONF = 'backend.urls'

CONTIFICO_BASE_URL = 'http://3.3.3.208:8080/api/v1/contifico/'

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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
     # 'default': {
     #     'ENGINE': 'django.db.backends.sqlite3',
     #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     # }
     'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'flitdb',
       'USER': 'root',
       'PASSWORD': 'root',
       'HOST': '127.0.0.1',
       'PORT': '5432',
       }
}

ASGI_APPLICATION = "backend.routing.application"

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# Custom user model
# AUTH_USER_MODEL = 'api.User'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
    'EXCEPTION_HANDLER': 'api.utils.custom_exception_handler'
    #'DEFAULT_PERMISSION_CLASSES': ('knox.views.IsAuthenticated',),
}

REST_KNOX = {
    # 'TOKEN_LIMIT_PER_USER': 6,
    'USER_SERIALIZER': 'api.serializers.UserSerializer',
    'TOKEN_TTL': timedelta(days=30)
}

FCM_DJANGO_SETTINGS = {
        "FCM_SERVER_KEY": "AIzaSyDIta0M1ebOcoMrRcpYON0HayFIF0JV4x0",
         # true if you want to have only one active device per registered user at a time
         # default: False
        "ONE_DEVICE_PER_USER": False,
         # devices to which notifications cannot be sent,
         # are deleted upon receiving error response from FCM
         # default: False
        "DELETE_INACTIVE_DEVICES": True,
}

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

# Local settings

try:
    from .local_settings import *
except ImportError:
    pass
