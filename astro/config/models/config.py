import os
from dotenv import load_dotenv, find_dotenv


class Config():
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    APP_NAME = "Astro"
    SECRET_KEY = os.environ.get("SECRET_KEY")
    TMDB_API_KEY = os.environ.get("TMDB_API_KEY")

    def __init__(self):
        load_dotenv(find_dotenv())
