from astro import db
from astro.base.models.base import Base


class Movie(db.Model, Base):
    title = db.Column(db.String(128))
    duration = db.Column(db.Integer)
    director = db.Column(db.String(120))
