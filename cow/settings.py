"""
Django settings for cow project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from corsheaders.defaults import default_headers

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ar^u#i3emzlc_9io1yk#e8w#k6k@47t+8pz4l%zz_c78%lya+x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = list(default_headers) + [
    'token'
]


# Application definition

INSTALLED_APPS = [
    'account',
    'business.project',
    'business.service',
    'component.gitlab',
    'asset.manager'

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'cow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'cow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

MYSQL_HOST = '192.168.51.207'
MYSQL_PORT = 3306
MYSQL_NAME = 'cuijianzhe'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'qwe*123456'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': MYSQL_HOST,
        'PORT': MYSQL_PORT,
        'NAME': MYSQL_NAME,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASSWORD,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_general_ci',
        },
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

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

# 有关celery配置
from kombu import Exchange, Queue
# celery configs
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'amqp://wenyang:wenyang@127.0.0.1:5672/cow')
CELERY_TIMEZONE = 'Asia/Shanghai'
# 一次在broker中取几个任务
CELERY_WORKER_PREFETCH_MULTIPLIER = 1

# 默认不记录结果
# 需要记录结果的任务，则单独指定ignore_result=False
# @celery_app.task(bind=True, ignore_result=False)
# CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'mongodb://localhost:27017/')
# CELERY_TASK_IGNORE_RESULT = True

CELERY_DEFAULT_QUEUE = 'default'
CELERY_TASK_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default', queue_arguments={'x-max-priority': 20}),
    Queue('low_priority', Exchange('low_priority'), routing_key='low_priority', queue_arguments={'x-max-priority': 10}),
    Queue('high_priority', Exchange('high_priority'), routing_key='high_priority', queue_arguments={'x-max-priority': 30}),
)

# 有关优先级队列启动问题
# celery  -A rurality worker -l info -n worker-hd1 -Q high_priority,default
# celery  -A rurality worker -l info -n worker-hd2 -Q high_priority,default
# celery  -A rurality worker -l info -n worker-hl1 -Q high_priority,low_priority
# 如果启动多个worker可以指定处理的队列，
# 示例中三个worker都可以处理高优先级队列，两个可以处理default队列，只有一个处理低优先级队列

CELERY_TASK_ROUTES = {
    'account.tasks.*': {'queue': 'high_priority'},
    '*': {"queue": 'default'},
}
# 除了上面可以不同任务指定不同队列外，在调用时也可以指定
# hello_task.apply_async(queue='low_priority')

# 定时任务，此命令只需要在一台机器上运行
# celery -A rurality beat -l info
CELERY_BEAT_SCHEDULE = {
    'timer_hello_task': {
        'task': 'account.tasks.timer_hello_task',
        'schedule': 10.0,
    },
}
