import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DB_CONNECTION = os.getenv("DB_CONNECTION")
