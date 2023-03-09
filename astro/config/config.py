import os
import platform
from dotenv import load_dotenv, find_dotenv


class Config:
    # TODO Fix the env variables to use dotenv
    # SECRET_KEY = os.environ.get("SECRET_KEY")
    # SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # STATIC_FOLDER = os.environ.get("STATIC_FOLDER")
    # IMAGE_ROOT = os.environ.get("IMAGE_ROOT")

    SECRET_KEY = "ko9bMII1YzHceERWCzDqcw"
    SQLALCHEMY_DATABASE_URI = "postgresql:///tux"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = "/public"
    IMAGE_ROOT = "public/files/img"

    PLATFORM_NAME = os.name
    PLATFORM_SYSTEM = platform.system(),
    PLATFORM_RELEASE = platform.release(),
    PLATFORM_MACHINE = platform.machine(),

    def __init__(self) -> None:
        load_dotenv(find_dotenv())
