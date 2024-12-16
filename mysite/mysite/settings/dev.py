from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-b!34rzoofoc$f&juul8#!qlyv70330#pe@(r2y$@a(al=y#h3s"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS = [
    *INSTALLED_APPS,
    "django_browser_reload",
]

MIDDLEWARE = [
    *MIDDLEWARE,
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]


try:
    from .local import *
except ImportError:
    pass
