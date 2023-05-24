from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTING_MODULE', 'restapi.settings')

app = Celery('restapi')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()