from datetime import datetime
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate(db)


def serialize(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return {k: v for k, v in obj.__dict__.items() if not k.startswith('_')}


def to_json(obj):
    json_str = json.dumps(obj, default=serialize)
    return json_str


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///astro"
    db.init_app(app)
    migrate.init_app(app)
    from astro.user.routes.user import user1
    print(type(user1))
    app.register_blueprint(user1)
    return app
