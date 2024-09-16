"""
Django settings for kolezzaSawaTok project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os  # This import was missing
import dj_database_url
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
import django_heroku

# from dotenv import load_dotenv, find_dotenv

# Load environment definition file
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Template directory
TEMPLATE_DIR = os.path.join(BASE_DIR, "kolezza_app", "templates")

# Security settings
SECRET_KEY = os.getenv("SECRET_KEY", "your-default-secret-key")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = ["*"]

SESSION_COOKIE_SECURE = True
CRSF_COOKIE_SECURE = True

LOGIN_URL = '/auth/login/'

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "speech_therapist",
    "child_management",
    "rest_framework",
    "child_module",
    "session",
    'api',
    "guardian",
    "level_of_stuttering",
    "users",
    "child_progress",
    "rest_framework.authtoken",
    "drf_yasg",
]

AUTHENTICATION_BACKENDS = [
     'django.contrib.auth.backends.ModelBackend',
     ]

AUTH_USER_MODEL = "users.User"

# Middleware configuration
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    
]

CSRF_TRUSTED_ORIGINS = []

ROOT_URLCONF = "kolezzaSawaTok.urls"

# Template configuration
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "kolezzaSawaTok.wsgi.application"


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

# Fallback for local development and test environments
if not os.getenv('DATABASE_URL'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
# Auth0 Configuration

AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN","")
AUTH0_CLIENT_ID = os.environ.get("AUTH0_CLIENT_ID","")
AUTH0_CLIENT_SECRET = os.environ.get("AUTH0_CLIENT_SECRET","")
REDIRECT_URI = os.environ.get("REDIRECT_URI","")

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type

# REST framework settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ]
}

SIMPLE_JWT = {
    'AUTH_COOKIE': 'access_token',  # Cookie name for storing the access token
    'AUTH_COOKIE_SECURE': False,    # Set to True in production
    'AUTH_COOKIE_HTTP_ONLY': True,  # HTTP-only cookie to prevent JavaScript access
    'AUTH_COOKIE_PATH': '/',        # Cookie available site-wide
    'AUTH_COOKIE_SAMESITE': 'Lax',  # Adjust SameSite settings as needed
}

SWAGGER_SETTINGS = {
    'DEFAULT_AUTO_SCHEMA_CLASS': 'drf_yasg.inspectors.SwaggerAutoSchema',
    'USE_SESSION_AUTH': False,  # Use token auth instead of session auth
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'REFETCH_SCHEMA_WITH_AUTH': True,
    'REFETCH_SCHEMA_ON_LOGOUT': True,
    'PERSIST_AUTH': True,
}

