"""
Django settings for personal_portfolio project.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings (for development only - change for production!)
SECRET_KEY = 'rc529@xt^_a4nl1j0y05btpr_3b+t7lla#a8xryms46phdgi#6'
DEBUG = False
ALLOWED_HOSTS = ['abdelrhmanbeseiso.pythonanywhere.com', '127.0.0.1']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
    'crispy_forms',
    'crispy_bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'personal_portfolio.urls'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = 'static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Added for global templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'personal_portfolio.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'abdelrhmanbeseiso$default',
        'USER': 'abdelrhmanbeseiso',
        'PASSWORD': 'Abood_$2288',  
        'HOST': 'abdelrhmanbeseiso.mysql.pythonanywhere-services.com',
    }
}
# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
import resend
# Option 1: Using Resend SMTP (recommended)
RESEND_API_KEY = 're_T688dGfy_3pEBNwwsSaEobur8HxfRU6xL'  
RESEND_FROM_EMAIL ="Abdelrhman Portfolio <onboarding@resend.dev>"  
RESEND_TO_EMAIL =["delivered@resend.dev"]

SECURE_SSL_REDIRECT = True          # Redirect HTTP → HTTPS
SESSION_COOKIE_SECURE = True        # Only send session cookies over HTTPS
CSRF_COOKIE_SECURE = True           # Only send CSRF cookies over HTTPS
SECURE_HSTS_SECONDS = 31536000      # Enable HSTS (1 year)
SECURE_HSTS_PRELOAD = True          
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
