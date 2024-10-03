from .base import *
import os


SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)

ROOT_URLCONF = 'core.urls'

# Host
ALLOWED_HOSTS = ['localhost', 'crmtiw.studioshouse.com', 'www.crmtiw.studioshouse.com']
CSRF_TRUSTED_ORIGINS = ['https://crmtiw.studioshouse.com', 'http://crmtiw.studioshouse.com']

# SECURE_SSL_REDIRECT = False # if True "You're accessing the development server over HTTPS, but it only supports HTTP."

SECURE_HSTS_SECONDS = 86400
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SESSION_COOKIE_AGE = 30000
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

AUTO_LOGOUT = {
    'IDLE_TIME': 30000,
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
    'MESSAGE': 'Sesja wygasła. Proszę zalogować się ponownie.',
    } 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crm',
    'management',
    'patients',

    'fontawesomefree',
    'phonenumber_field',

    'turnstile',

    'login_history',

    'dbbackup',

]

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR / 'core/db/backup'}

# Local database
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'core/db/db.sqlite3',
    },

# Neon database
    'neon_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('PGDATABASE'),
        'USER': env('PGUSER'),
        'PASSWORD': env('PGPASSWORD'),
        'HOST': env('PGHOST'),
        'PORT': 5432,
        'OPTIONS': {'sslmode': 'require',},
    },

# Postgres Unraid database
    'postgres_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'), # name of databsae
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    },
}



DATABASE_ROUTERS = [
    # 'core.settings.routers.CloudAppRouter',
    # 'core.settings.routers.LocalAppRouter',
    'core.settings.routers.NeonAppRouter',
    ]

# Cloudflare storages
# AWS_STORAGE_BUCKET_NAME = env('BUCKET_NAME')
# AWS_S3_ENDPOINT_URL = env('BUCKET_ID')
# AWS_S3_ACCESS_KEY_ID = env('BUCKET_ACCES_KEY')
# AWS_S3_SECRET_ACCESS_KEY = env('BUCKET_SECRET_KEY')
# AWS_S3_SIGNATURE_VERSION = 's3v4'
# AWS_S3_FILE_OVERWRITE = False
# STORAGES = {
#     # Media file (image) management   
#     "default": {
#         "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
#     },
#     # CSS and JS file management
#     "staticfiles": {
#         "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
#     },
# }

# Hcaptcha
HCAPTCHA_SITEKEY = env('HCAPTCHA_SITEKEY')
HCAPTCHA_SECRET = env('HCAPTCHA_SECRET')
HCAPTCHA_TIMEOUT = 5

# Cloudflare
TURNSTILE_SITEKEY = env('TURNSTILE_SITEKEY')
TURNSTILE_SECRET = env('TURNSTILE_SECRET')
TURNSTILE_JS_API_URL = 'https://challenges.cloudflare.com/turnstile/v0/api.js'
TURNSTILE_VERIFY_URL = 'https://challenges.cloudflare.com/turnstile/v0/siteverify'
TURNSTILE_TIMEOUT = 5

# Google
RECAPTCHA_PUBLIC_KEY = env('PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = env('PRIVATE_KEY')
# RECAPTCHA_USE_SSL = True