import os
import secrets
from config.database import DatabaseConfig
from config.email import EmailConfig
from config.log import LogConfig
from config.project import ProjectConfig
import string


alphabet = string.ascii_letters + string.digits


class AppConfig(DatabaseConfig, ProjectConfig, LogConfig, EmailConfig):
    APP_NAME = os.environ.get("APP_NAME", "medusa")
    APP_ENV = os.environ.get("APP_ENV", "development")
    SECRET_KEY = ''.join(secrets.choice(alphabet) for i in range(32))
    DEBUG = False
