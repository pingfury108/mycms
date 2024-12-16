import os

from .base import *

DEBUG = False

SECRET_KEY = "django-insecure-b!34rzoofoc$f&juul8#!qlyv70330#pe@(r2y$@a(al=y#h3s"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",") or []

try:
    from .local import *
except ImportError:
    pass
