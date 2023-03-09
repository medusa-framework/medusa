from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import coloredlogs
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__, static_url_path="/public")
    with app.app_context():
        from . import config
        app.config.from_object(config.config.Config)
        app.static_url_path = app.config.get("STATIC_FOLDER")
        app.static_folder = app.root_path + app.static_url_path
        db.init_app(app)
        migrate.init_app(app)
        bcrypt.init_app(app)
        login_manager.init_app(app)
        app.extensions["migrate"].db = db
        coloredlogs.install()
        from . import modules
        return app


app = create_app()
