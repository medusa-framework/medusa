from faker import Faker
from medusa.modules.app.base.controllers.base import BaseController
from medusa.modules.app.base.models.base import Base
from medusa.modules.app.user.seeders.access_right import access_rights as seeds
from medusa import db


class AccessRight(Base, db.Model):
    name = db.Column(db.String())

    def __init__(self) -> None:
        self._controller = BaseController(self)
        self._seeds = seeds
        super().__init__()

    def factory(self):
        faker = Faker()
        name = faker.word()
        json = {"name": name}
        return json


AccessRight()
