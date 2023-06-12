"""
Django settings for garment project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from django.contrib.messages import constants as messages
from pathlib import Path
# sect25-len117
from decouple import config

import dj_database_url



import os



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

#NEW Render


import environ

env = environ.Env()
environ.Env.read_env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# .env
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# .env
#ORIGINAL 
DEBUG = config('DEBUG', default=True, cast=bool)  # True
#DEBUG = config('DEBUG', cast=bool)

#FOR aws
#ALLOWED_HOSTS = []
#    'brand-env.eba-bepcfz6j.us-west-2.elasticbeanstalk.com', '*', 'brandshop.se'


#ALLOWED_HOSTS = ['other-brand.onrender.com', 'localhost', '127.0.0.1']
ALLOWED_HOSTS = ['*']

# Application definition
#-ADD whitenoise
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'category',
    'accounts',
    'store',
    'carts',
    'orders',
  
]

#ADD whitenoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    
    
]

# -sect15-len-119 SESSION_EXPIRE,SESSION_TIMEOUT
SESSION_EXPIRE_SECONDS = 3600  # 1 hour
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_TIMEOUT_REDIRECT = 'accounts/login'


ROOT_URLCONF = 'garment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'carts.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'garment.wsgi.application'

# from accounts models py
AUTH_USER_MODEL = 'accounts.Account'

 
#DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.sqlite3',
#            'NAME': BASE_DIR / 'db.sqlite3',
#        }
#    }

#Render
#DATABASES = {
#    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))

#}
'''
#________
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://...',
        conn_max_age=600,
        conn_health_checks=True,
    )
}
'''   
#__________________________
'''
#DATABASES = {
#    'default': dj_database_url.config(
#        'postgres://...',
#        conn_max_age=600,
#        conn_health_checks=True,
#    )
#}
'''
#____________-
'''
import dj_database_url

DATABASES = {

    'default': dj_database_url.parse(env('DATABASE_URL'))
     
}
'''
#-----------------------
if 'DATABASE_URL' in os.environ:
 
    DATABASES = {
        'default': dj_database_url.parse(env('DATABASE_URL'))
    } 

else:
   print("Postgres URL found, using sqlite instead")


DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/



STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
   'garment/static',
]

#ADD STATICFILES_STORAGE
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'






# --media file configuration --upload image in the admin
# --go to web-garment root folder url py setup the path
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -django alert messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# -SMTP configuration .env
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)

#DATABASE_URL = config('DATABASE_URL')

#NEW-> to remove the WARNING in the terminal
DEFAULT_AUTO_FIELD='django.db.models.AutoField'
