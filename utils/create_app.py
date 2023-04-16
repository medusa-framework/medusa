from flask import Flask
import os
from config.app import db, migrate, seeder, login_manager, bcrypt
from utils.init_models import init_modules
from config.app import config
import coloredlogs

modules_path = os.environ.get("MODULES_PATH", "/home/jacob/code/yentl/modules")


def create_app(env="development"):
    coloredlogs.install()
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(config[os.environ.get("APP_ENV", env)])
        db.init_app(app)
        migrate.init_app(app, db)
        seeder.init_app(app, db)
        bcrypt.init_app(app)
        login_manager.init_app(app)
        db.create_all()
        init_modules(modules_path)
        return app
