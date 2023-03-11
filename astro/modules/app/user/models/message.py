from faker import Faker
from astro import db
from astro.modules.app.base.controllers.base import BaseController
from astro.modules.app.base.models.base import Base
from flask_login import current_user


class Message(Base, db.Model):
    message = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self) -> None:
        self._controller = BaseController(self)
        super().__init__()

    def create(self, **kwargs):
        if not kwargs.get("user_id"):
            kwargs["user_id"] = current_user.id
        return super().create(json=kwargs)

    def factory(self):
        json = {
            "user_id": current_user.id,
            "message": Faker().sentence(),
        }
        return json


Message()
