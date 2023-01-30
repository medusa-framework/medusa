from astro import db
from astro.base.models.base import Base
from flask_login import current_user


class Comment(db.Model, Base):
    message = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def create(self, json=None, **kwargs):
        return super().create(user_id=current_user.id)
