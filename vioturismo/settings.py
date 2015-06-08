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
#   'django_extensions',
    'vioturismo.apps.sitios',
    'vioturismo.apps.sturist',
    'vioturismo.apps.webServices.wsSitiostcs',
#    'django.contrib.admindocs',

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

AUTH_PROFILE_MODULE = 'sitios.userProfile'

WSGI_APPLICATION = 'vioturismo.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}





# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#MANAGERS = ADMINS
#MOTOR_DB == 'sqlite'


#if MOTOR_DB == 'mysql':
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'vio',
#        'USER': 'root',                      # Nol at used with sqlite3.
#        'PASSWORD': 'root',                  # Not used with sqlite3.
#        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',  
#    }
#}
#if MOTOR_DB == 'sqlite':
#    DATABASES = {
#       'default': {
#           'ENGINE': 'django.db.backends.sqlite3',
#           'NAME': os.path.join(os.path.dirname(__file__),'vio.db'),
#           'USER': 'root',                      # Nol at used with sqlite3.
#           'PASSWORD': 'root',                  # Not used with sqlite3.
#           'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#           'PORT': '',  
#       }
#   }





LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



#MEDIA_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__),'media/'))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS =(
    BASE_DIR + '/static',
    #os.path.join(BASE_DIR+'/static/'),

)


TEMPLATE_DIRS = (
    BASE_DIR + '/templates/',
)



#TEMPLATE_DIRS = (
#    BASE_DIR + '/templates',
#    os.path.join(BASE_DIR+'/templates/'),

#)


#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


LOGIN_REDIRECT_URL = '/'


# AQUI VA LA CONFIGURACION DEL SERVIDOR DE CORREO
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465 
EMAIL_HOST_USER = 'vioturismopro@gmail.com'
EMAIL_HOST_PASSWORD = 'Jn123456'
EMAIL_USE_TLS = True
#587

URL_LOGIN = '/login/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
#import os
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)
