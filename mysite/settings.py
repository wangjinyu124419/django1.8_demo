# -*- coding: utf-8 -*-

"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6h88(4m0rk&ub^^s0=%pv+tu#0%960xrg68*ats#tzvxwg&6a+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = "new_users.CmsUser"

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'polls_2',
    'new_users',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        #DIRS默认为空
        # 'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases



"""
python manage.py migrate 会在default中的空的mysql数据库中创建
auth_group、auth_user、django_migrations等10张table，
python manage.py createsuperuser生成的管理员用户数据会催到auth_user表中

"""


# DATABASE_ROUTERS = ['mysite.database_router.Router',]
DATABASES = {
    #mysql配置
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'demo',
        'USER': 'root',
        'PASSWORD': '124419',
        'HOST': '127.0.0.1',
        'PORT': '3306',

        #默认
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'demo2': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'demo2',
        'USER': 'root',
        'PASSWORD': '124419',
        'HOST': '127.0.0.1',
        'PORT': '3306',
}
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
#默认时区
# TIME_ZONE = 'UTC'

#中国时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

#默认为True
#USE_TZ = True
#改为False后mysql时区才与TIME_ZONE的设置同步
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Django Suit',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
       'sites': 'icon-leaf',
       'auth': 'icon-lock',
    },
    'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        # 'sites',
        {'app': 'auth', 'icon': 'icon-lock'},

        # {'app': 'auth', 'icon':'icon-lock', 'models': ('new_users' 'groups')},
        {'app': 'new_users', 'icon':'icon-lock'},
        {'app': 'polls', 'label': 'polls', 'icon': 'icon-file', 'models': (
            'Question','Choice',

        )},
        {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
        {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    ),

    # misc
    'LIST_PER_PAGE': 15
}

# TEMPLATE_CONTEXT_PROCESSORS = TCP + (
#     'django.core.context_processors.request',
# )