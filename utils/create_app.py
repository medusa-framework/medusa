import os
import coloredlogs
from flask import Flask
from config.app import db, migrate, seeder, login_manager, bcrypt
from config.app import config
from utils.init_models import init_modules


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
        init_modules(app.config.get("MODULES_DIR"))
        return app
