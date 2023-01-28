import os
from dotenv import load_dotenv, find_dotenv


class Config():
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    APP_NAME = "Astro"

    def __init__(self):
        load_dotenv(find_dotenv())
