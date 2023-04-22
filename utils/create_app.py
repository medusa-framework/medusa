import os
import coloredlogs
from flask import Flask
from config.system import db, migrate, seeder, login_manager, bcrypt, mail
from config.environment import config
from utils.init_models import init_modules


def create_app(env="development"):
    coloredlogs.install()
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(config[os.environ.get("APP_ENV", env)])
        db.init_app(app)
        migrate.init_app(app, db)
        mail.init_app(app)
        seeder.init_app(app, db)
        bcrypt.init_app(app)
        login_manager.init_app(app)
        db.create_all()
        init_modules(app.config.get("MODULES_DIR"))
        return app
