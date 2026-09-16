import os
from dotenv import load_dotenv

# ЭТА СТРОКА КРИТИЧЕСКИ ВАЖНА: она читает файл .env
load_dotenv()


class Config:
    # Берем значение из .env
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
