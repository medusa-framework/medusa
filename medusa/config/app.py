import os
import secrets
from medusa.config.database import DatabaseConfig
from medusa.config.database import build_sqlalchemy_uri


class Config(DatabaseConfig):
    """
    Base configuration class for the Flask app.

    Attributes:
        APP_NAME (str): The name of the Flask application. Defaults to "medusa".
        FLASK_APP (str): The path to the Flask app module. Defaults to "run.py".
        SECRET_KEY (str): Secret key used by the Flask app to encrypt session data.
        DEBUG (bool): Determines if the Flask app is in debug mode. Defaults to False.
    """

    APP_NAME = os.environ.get("APP_NAME", "medusa")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "medusa")
    FLASK_APP = os.environ.get("FLASK_APP", "run.py")
    SECRET_KEY = os.environ.get("SECRET_KEY", secrets.token_bytes(32))
    DEBUG = False
    # TODO: if last 4 of log name is not '.log', append .log
    LOG_NAME = os.environ.get(
        "LOG_NAME", APP_NAME.lower().replace(" ", "_"))
    LOG_PATH = os.environ.get("LOG_PATH", "/logs")
    LOG_FILE = os.environ.get("LOG_FILE", f"{LOG_PATH}/{LOG_NAME}.log")


class DevelopmentConfig(Config):
    """
    Configuration class for the Flask app in development environment.

    Attributes:
        DEBUG (bool): Determines if the Flask app is in debug mode. Defaults to True.
        SQLALCHEMY_DATABASE_URI (str): URI to connect to the development database.
    """

    DEBUG = True
    DATABASE_NAME = os.environ.get(
        "DATABASE_NAME_DEVELOPMENT", f"{Config.DATABASE_NAME}_development"
    )
    SQLALCHEMY_DATABASE_URI = build_sqlalchemy_uri(DATABASE_NAME)


class TestingConfig(Config):
    """
    Configuration class for the Flask app in testing environment.

    Attributes:
        TESTING (bool): Determines if the Flask app is in testing mode. Defaults to True.
        SQLALCHEMY_DATABASE_URI (str): URI to connect to the testing database.
    """

    TESTING = True
    DATABASE_NAME = os.environ.get(
        "DATABASE_NAME_TESTING", f"{Config.DATABASE_NAME}_testing"
    )
    SQLALCHEMY_DATABASE_URI = build_sqlalchemy_uri(DATABASE_NAME)


class ProductionConfig(Config):
    """
    Configuration class for the Flask app in production environment.

    Attributes:
        SQLALCHEMY_DATABASE_URI (str): URI to connect to the production database.
    """

    DATABASE_NAME = os.environ.get("DATABASE_NAME", Config.DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = build_sqlalchemy_uri(DATABASE_NAME)


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
