import os

import dj_database_url
from decouple import Csv, config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default="secret")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*", cast=Csv())

SITE_ID = 1

ADMIN_EMAILS = config("ADMIN_EMAILS", default="", cast=Csv())


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "django_extensions",
    "django_countries",
    "multiselectfield",
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "drf_yasg",
    "compressor",
    "compressor_toolkit",
    "data",
    "invitations",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = ("127.0.0.1",)

ROOT_URLCONF = "sixstripes_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "sixstripes_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    "default": (
        dj_database_url.parse(
            config("DATABASE_URL", default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3"))
        )
    )
}


# Pasord validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_HOST = config("DJANGO_STATIC_HOST", default="")
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "public/static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

NODE_BIN = os.path.join(os.path.dirname(BASE_DIR), "node_modules/.bin")
COMPRESS_NODE_SASS_BIN = os.path.join(NODE_BIN, "node-sass")
COMPRESS_POSTCSS_BIN = os.path.join(NODE_BIN, "postcss")
COMPRESS_BROWSERIFY_BIN = os.path.join(NODE_BIN, "webpack")

COMPRESS_ES6_COMPILER_CMD = (
    "{browserify_bin} {infile} -o {outfile}"
    # 'export NODE_PATH="{paths}" && '
    # '{browserify_bin} {infile} -o {outfile} '
    # '-t [ "{node_modules}/babelify" --presets=[ {node_modules}/@babel/preset-env ] ]'
    # '-t [ "{node_modules}/babelify" --presets=[ {node_modules}/@babel/preset-env ] ]'
)

COMPRESS_PRECOMPILERS = (
    ("text/scss", "compressor_toolkit.precompilers.SCSSCompiler"),
    ("module", "compressor_toolkit.precompilers.ES6Compiler"),
)


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
}


EMAIL_BACKEND = config("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
EMAIL_HOST = config("EMAIL_HOST", default="localhost")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=True, cast=bool)
EMAIL_PORT = config("EMAIL_PORT", default=25, cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="Webmaster <webmaster@localhost>")


SWAGGER_SETTINGS = {"SECURITY_DEFINITIONS": {}}
