from ..env import env

REDIS_URL = env("REDIS_URL")
REDIS_LOCK_DB = env("REDIS_LOCK_DB", default="6")
