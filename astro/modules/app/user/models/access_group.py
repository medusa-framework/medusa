from astro.modules.app.base.controllers.base import BaseController
from astro.modules.app.base.models.base import Base
from astro import db


class AccessGroup(Base, db.Model):
    name = db.Column(db.String())

    def __init__(self) -> None:
        self._controller = BaseController(self)
        super().__init__()


AccessGroup()
