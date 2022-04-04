from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loyalty.settings')

app = Celery('loyalty')


app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'count_balance_every_1_minute': {
        'task': 'operations.tasks.count_balance_beat',
        'schedule': crontab(minute='*/1'),
    },
}
