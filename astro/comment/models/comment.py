from astro import db
from astro.base.models.base import Base


class Comment(db.Model, Base):
    message = db.Column(db.String())
    user_id = db.Column(db.Integer)
