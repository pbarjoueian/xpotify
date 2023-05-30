from ..env import env

CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")

CELERY_BEAT_SCHEDULE = {
    # "sync_all_placements": {
    #     "task": "syncer.tasks.sync_all_placements",
    #     "schedule": 2 * MINUTS_SECONDS_CONSTANT,
    # },
}
