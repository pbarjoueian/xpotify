from celery.schedules import crontab

from ..env import env

CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")

CELERY_BEAT_SCHEDULE = {
    "run_tracks_clustering": {
        "task": "ml.tasks.run_tracks_clustering",
        "schedule": crontab(minute="0", hour="*/1"),
    },
}
