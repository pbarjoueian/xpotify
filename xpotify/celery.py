import os

from celery import Celery

from xpotify import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xpotify.settings")

app = Celery("xpotify")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.timezone = "UTC"

app.conf.task_default_queue = "default"

app.conf.beat_schedule = settings.CELERY_BEAT_SCHEDULE

app.conf.task_default_exchange = "tasks"
app.conf.task_default_exchange_type = "topic"

app.conf.ONCE = {
    "backend": "celery_once.backends.Redis",
    "settings": {
        "url": settings.REDIS_URL,
        "default_timeout": 60 * 60 * 5,  # after 2 weeks release the lock
    },
}
