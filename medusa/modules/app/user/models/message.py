from faker import Faker
from medusa import db
from medusa.modules.app.base.controllers.base import BaseController
from medusa.modules.app.base.models.base import Base
from flask_login import current_user


class Message(Base):
    # message = db.Column(db.String())
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self) -> None:
        self._controller = BaseController(self)
        super().__init__()

    def factory(self):
        json = {
            "user_id": current_user.id,
            "message": Faker().sentence(),
        }
        return json


Message()
