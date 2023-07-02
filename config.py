import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    HOST = os.environ.get('HOST')
    PORT = os.environ.get('PORT')


class APIConfig:
    TOKEN = os.environ.get('TOKEN')
    MAIN_API = os.environ.get('MAIN_API')
    API_MAIN_ENDPOINT = os.environ.get('API_MAIN_ENDPOINT')
