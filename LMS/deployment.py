import os
from .settings import *
from .settings import BASE_DIR
SECRET_KEY='w7a8555a@lj8nax7tem0caa2f2rjm2ahsascyf83sa5alyv68vea'#os.environ['SECRET']
ALLOWED_HOSTS = ['technokraftzonline.azurewebsites.net', 'technokraftz.com', '*'] #[os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS=['https://'+ os.environ['WEBSITE_HOSTNAME']]
DEBUG=False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
   # 'app.middleware.AdBlockerMiddleware',
    #'django.contrib.staticfiles.middleware.StaticFilesMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media','media')
STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


connection_string=os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
parameters = {pair.split('=')[0]: pair.split('=')[1] for pair in connection_string.split(',')}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': parameters['dbname'],
#         'HOST': parameters['host'],
#         'USER': parameters['user'],
#         'PASSWORD': parameters['password'],
#         'OPTIONS': {'sslmode': 'require'},
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'technokraftzonline-database',
        'HOST': 'technokraftzonline-server.postgres.database.azure.com',
        'USER': 'xhzjzieman',
        'PASSWORD': 'FO16A4AM85F2ZWR5$',
        'OPTIONS': {'sslmode': 'require'},
    }
}

