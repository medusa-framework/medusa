from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os
from config.database import DatabaseConfig, build_sqlalchemy_uri
import secrets
import string


db = SQLAlchemy()
migrate = Migrate()
seeder = FlaskSeeder()
bcrypt = Bcrypt()
login_manager = LoginManager()
alphabet = string.ascii_letters + string.digits


class Config(DatabaseConfig):
    APP_NAME = os.environ.get("APP_NAME", "medusa")
    PROJECT_DIR = os.path.abspath(os.getcwd())
    MODULES_DIR = f"{PROJECT_DIR}/modules"
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "medusa")
    SECRET_KEY = ''.join(secrets.choice(alphabet) for i in range(32))
    DEBUG = False
    # TODO: if last 4 of log name is not '.log', append .log
    LOG_NAME = os.environ.get(
        "LOG_NAME", APP_NAME.lower().replace(" ", "_"))
    LOG_DIR = os.environ.get("LOG_DIR", "/logs")
    LOG_FILE = os.environ.get("LOG_FILE", f"{LOG_DIR}/{LOG_NAME}.log")


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_NAME = os.environ.get(
        "DATABASE_NAME_DEVELOPMENT", f"{Config.DATABASE_NAME}_development"
    )
    SQLALCHEMY_DATABASE_URI = build_sqlalchemy_uri(DATABASE_NAME)


class TestingConfig(Config):
    TESTING = True
    DATABASE_NAME = os.environ.get(
        "DATABASE_NAME_TESTING", f"{Config.DATABASE_NAME}_testing"
    )
    SQLALCHEMY_DATABASE_URI = build_sqlalchemy_uri(DATABASE_NAME)


class ProductionConfig(Config):
    DATABASE_NAME = os.environ.get("DATABASE_NAME", Config.DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = build_sqlalchemy_uri(DATABASE_NAME)


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
