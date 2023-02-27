from astro import db
from astro.modules.app.base.models.base import Base
from astro.modules.custom.genre.seeders.genre import genres as seeds


class Genre(db.Model, Base):
    name = db.Column(db.String)
