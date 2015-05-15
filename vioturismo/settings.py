import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



SECRET_KEY = 'v!q#6g(en1_!f1=bfh0c%qy(!krrou%0y!m)ee8s27#nwecdar'


DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'vioturismo.apps.sitios',
    'vioturismo.apps.sturist'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'vioturismo.urls'

AUTH_PROFILE_MODULE = 'vioturismo.sitios.userProfile'

WSGI_APPLICATION = 'vioturismo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vio',
        'USER': 'root',                      # Nol at used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  
    }
}

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



MEDIA_URL = '/media/'
MEDIA_ROOT =os.path.join(BASE_DIR, 'vioturismo/media')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS =(
    os.path.join(BASE_DIR+'/static/'),

)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR+'/templates/'),

)


