import os
from utils.build_sqlalchemy_uri import build_sqlalchemy_uri


class DatabaseConfig:
    DATABASE_TYPE = os.environ.get("DATABASE_TYPE", "sqlite")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Medusa")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = build_sqlalchemy_uri(
        DATABASE_TYPE, DATABASE_NAME
    )
