#encoding:utf-8
from __future__ import absolute_import
"""
Django settings for sistema_consulta project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

RUTA_TEMPLATES = os.path.join(BASE_DIR, 'templates')


TEMPLATE_DIRS = (RUTA_TEMPLATES,)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e6tzjw)*7&6i6pxp7gfmhj)5o5jy!ev1dek!76uqxxxa5q0-*0'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG

##DEBUG = True
##TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'pixelfields_smart_selects',
    'django_extensions',
    'apps.topologia.estados',
    'apps.topologia.municipios',
    'apps.topologia.parroquias',
    'apps.centro_votacion', # Api para centro de votacion
    'apps.login',
    'apps.registro', # Api para centro de votacion
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'sistema_consulta.urls'

WSGI_APPLICATION = 'sistema_consulta.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sistema_consulta1',
        'USER': 'sisconsulta',
        'PASSWORD': '$iSc0nsU7t@',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Configuraciones de rest framework
REST_FRAMEWORK = {  # Filtrado
    #'DEFAULT_FILTER_BACKENDS': (
    #    'rest_framework.filters.DjangoFilterBackend',
    #),
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    #'DEFAULT_MODEL_SERIALIZER_CLASS': (
    #    'rest_framework.serializers.HyperlinkedModelSerializer',
    #'rest_framework.permissions.IsAuthenticated',
    #),
    # Use Django's standard 'django.contrib.auth' permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        #'rest_framework.permissions.IsAuthenticated',
    ),

    #'DEFAULT_AUTHENTICATION_CLASSES': (
    #    'rest_framework.authentication.BasicAuthentication',
    #),
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-VE'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = '/home/administrador/django/sistema_consulta/static/'
STATIC_URL ='http://consultaelectoral.bva.org.ve/static/'
#STATIC_URL = '/static/'


RUTA_STATIC = os.path.join(BASE_DIR, 'static')

#STATICFILES_DIRS = (RUTA_STATIC,)
############################################################################
#                         Habilitar esta linea para cors
############################################################################
CORS_ORIGIN_ALLOW_ALL = True
############################################################################
