from datetime import datetime
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from astro.config.models.config import Config
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
migrate = Migrate(db)
login_manager = LoginManager()
bcrypt = Bcrypt()


def serialize(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return {k: v for k, v in obj.__dict__.items() if not k.startswith('_')}


def to_json(obj):
    json_str = json.dumps(obj, default=serialize)
    return json_str


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    from astro.user.routes.user import user
    from astro.movie.routes.movie import movie
    from astro.comment.routes.comment import comment
    app.register_blueprint(user, url_prefix="/api/user")
    app.register_blueprint(movie, url_prefix="/api/movie")
    app.register_blueprint(comment, url_prefix="/api/comment")
    print(Config().APP_NAME)
    return app
