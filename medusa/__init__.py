import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import coloredlogs
from flask_bcrypt import Bcrypt
from medusa.config.app import Config, config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app(env="development"):
    """
    Creates and returns a Flask application instance, initializing the necessary extensions.

    Args:
        env (str): The environment to run the application in.

    Returns:
        Flask: The Flask application instance.
    """
    app = Flask(__name__, static_url_path="/public")

    # Initialize the application context and configuration.
    with app.app_context():
        # Set the application configuration based on the environment.
        app.config.from_object(config[os.environ.get("APP_ENV", env)])
        # Set the static URL path for the application.
        app.static_url_path = app.config.get("STATIC_FOLDER")
        # Set the static folder path for the application.
        app.static_folder = app.root_path + app.static_url_path

        # Initialize the SQLAlchemy database, migration manager, Bcrypt encryption, and login manager extensions.
        db.init_app(app)
        migrate.init_app(app, db)
        bcrypt.init_app(app)
        login_manager.init_app(app)

        # Install colored logging.
        coloredlogs.install()

        # Import application modules.
        from . import modules

        # Create the database tables.
        db.create_all()

        # Return the Flask application instance.
        return app


# Create a Flask application instance using the default environment.
app = create_app()
