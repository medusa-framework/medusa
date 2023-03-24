import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import coloredlogs
from flask_bcrypt import Bcrypt
from medusa.config.app import config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app(env="development"):
    app = Flask(__name__, static_url_path="/public")
    with app.app_context():
        app.config.from_object(
            config[os.environ.get("APP_ENV", env)])
        app.static_url_path = app.config.get("STATIC_FOLDER")
        app.static_folder = app.root_path + app.static_url_path
        db.init_app(app)
        migrate.init_app(app, db)
        bcrypt.init_app(app)
        login_manager.init_app(app)
        coloredlogs.install()
        from . import modules
        db.create_all()
        return app


app = create_app()
