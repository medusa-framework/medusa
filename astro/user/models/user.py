from astro import db
from astro.base.models.base import Base


class User(db.Model, Base):
    username = db.Column(db.String(128))
    password = db.Column(db.String())
    email = db.Column(db.String(120))
