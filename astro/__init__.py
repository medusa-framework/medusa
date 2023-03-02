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
    app = Flask(__name__)
    with app.app_context():
        from .config.models.config import Config
        app.config.from_object(Config)
        db.init_app(app)
        migrate.init_app(app)
        bcrypt.init_app(app)
        login_manager.init_app(app)
        app.extensions["migrate"].db = db
        app.config["SERVER_NAME"] = "192.168.253.128:5000"
        coloredlogs.install()
        from . import modules
        # from astro.modules.app.user.routes.user import user
        # from astro.modules.custom.movie.routes.movie import movie
        # from astro.modules.app.comment.routes.comment import comment
        # from astro.modules.custom.genre.routes.genre import genre
        # from astro.modules.app.language.routes.language import language
        # from astro.modules.custom.person.routes.person import person
        # from astro.modules.app.sandbox.routes.sandbox import sandbox
        # app.register_blueprint(user, url_prefix="/api/user")
        # app.register_blueprint(movie, url_prefix="/api/movie")
        # app.register_blueprint(comment, url_prefix="/api/comment")
        # app.register_blueprint(genre, url_prefix="/api/genre")
        # app.register_blueprint(language, url_prefix="/api/language")
        # app.register_blueprint(person, url_prefix="/api/person")
        # app.register_blueprint(sandbox, url_prefix="/api/sandbox")
        print(app.config["SERVER_NAME"])
        return app


app = create_app()
