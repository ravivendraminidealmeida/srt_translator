import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DB_CONNECTION = os.getenv("DB_CONNECTION")
TOKEN_EXPIRATION_TIME_IN_HOURS = os.getenv("TOKEN_EXPIRATION_TIME_IN_HOURS")

