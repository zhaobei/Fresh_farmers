"""
Django settings for dailyfresh project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

import raven
import toml
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# ENV_MODE = os.environ.get('ENV_MODE')
with open('./config/config_env.toml') as f:
    config = toml.load(f)

#mysql
ENV_DATABASE_ENGINE = config['database']['engine']
ENV_DATABASE_USER = config['database']['user']
ENV_DATABASE_PASSWORD = config['database']['password']
ENV_DATABASE_HOST = config['database']['host']
ENV_DATABASE_PORT = config['database']['port']
ENV_DATABASE_NAME = config['database']['database']


# redis
ENV_REDIS_HOST = config['redis']['host']
ENV_REDIS_PORT = config['redis']['port']


# Email
ENV_EMAIL_BACKEND = config['Email']['EMAIL_BACKEND']
ENV_EMAIL_HOST = config['Email']['EMAIL_HOST']
ENV_EMAIL_PORT = config['Email']['EMAIL_PORT']
ENV_EMAIL_HOST_PASSWORD = config['Email']['EMAIL_HOST_PASSWORD']
ENV_EMAIL_HOST_USER = config['Email']['EMAIL_HOST_USER']
ENV_EMAIL_FROM = config['Email']['EMAIL_FROM']


# Case_django
ENV_CACHES_BACKEND = config['case']['BACKEND']
ENV_CACHES_LOCATION = config['case']['LOCATION']
ENV_OPTIONS_BACKEND = config['case']['CLIENT_CLASS']


# fdfs
ENV_FDFS_CLIENT_CONF = config['fdfs']['FDFS_CLIENT_CONF']
ENV_FDFS_URL = config['fdfs']['FDFS_URL']






# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#设置路径

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l1$ip-%%4w)wza&t$nd_ok5imd88n4y6y6dk%$u26s=z=n^las'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = "*"


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack', # 注册全文检索的框架
    'tinymce', # 富文本编辑器
    'apps.user', # 用户模块
    'apps.goods', # 商品模块
    'apps.cart', # 购物车模块
    'apps.order', # 订单模块
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

ROOT_URLCONF = 'dailyfresh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'dailyfresh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': ENV_DATABASE_ENGINE,
        'NAME': ENV_DATABASE_NAME,
        'USER': ENV_DATABASE_USER,
        'PASSWORD': ENV_DATABASE_PASSWORD ,
        'HOST': ENV_DATABASE_HOST,
        'PORT':ENV_DATABASE_PORT,
    }
}
# django 认证系统使用的模型类
AUTH_USER_MODEL='user.User'


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/


LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]  DEBUG=False时需要STATIC_ROOT，需要在url配置静态文件路由缺一不可
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#  富文本编辑器的配置
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}


# 发送邮件配置
EMAIL_BACKEND = ENV_EMAIL_BACKEND
# smpt服务地址
EMAIL_HOST = ENV_EMAIL_HOST
EMAIL_PORT = ENV_EMAIL_PORT
# 发送邮件的邮箱
EMAIL_HOST_USER = ENV_EMAIL_HOST_USER
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = ENV_EMAIL_HOST_PASSWORD
# 收件人看到的发件人
EMAIL_FROM = ENV_EMAIL_FROM


# Django的缓存配置
CACHES = {
    "default": {
        "BACKEND": ENV_CACHES_BACKEND,
        "LOCATION": ENV_CACHES_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS":ENV_OPTIONS_BACKEND,
        }
    }
}

# 配置session存储
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS  = "default"

# 配置url地址
LOGIN_URL='/user/login'

# 设置Django的文件存储类
# DEFAULT_FILE_STORAGE='utils.fdfs.storage.FDFSStorage'
DEFAULT_FILE_STORAGE='utils.fdfs.storage.FDFSStorage'



# 设置fdfs使用的client.conf文件路径
FDFS_CLIENT_CONF = ENV_FDFS_CLIENT_CONF
# 设置fdfs存储服务器上nginx的IP和端口号
FDFS_URL = ENV_FDFS_URL

# 全文检索框架的配置
HAYSTACK_CONNECTIONS = {
    'default': {
        #使用whoosh引擎
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        #'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        #索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

#当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# 指定搜索结果每页显示的条数
HAYSTACK_SIGNAL_RESULTS_PER_PAGE=1
