from astro import db
from astro.base.models.base import Base
import requests
from flask import current_app
from astro.genre.seeders.genre import genres as seeds


class Genre(db.Model, Base):
    name = db.Column(db.String)
