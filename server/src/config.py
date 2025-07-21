import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

DB_CONNECTION = os.getenv("DB_CONNECTION")

TOKEN_EXPIRATION_TIME_IN_HOURS = os.getenv("TOKEN_EXPIRATION_TIME_IN_HOURS")

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

UNPROTECTED_ENDPOINTS = [
    'login',
    'signup'
]

CELERY_CONFIG = dict(
    broker_url="redis://localhost:6379/0",
    result_backend="redis://localhost:6379/0",
    task_ignore_result=True,
)

DEFAULT_FROM_LANG = 'en'
DEFAULT_TO_LANG = 'pt'

