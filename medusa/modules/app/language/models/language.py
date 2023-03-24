from medusa import db
from medusa.modules.app.base.controllers.base import BaseController
from medusa.modules.app.base.models.base import Base
from medusa.modules.app.language.seeders.language import languages as seeds


class Language(Base, db.Model):
    name = db.Column(db.String)
    iso_639_1 = db.Column(db.String)
    english_name = db.Column(db.String)

    def __init__(self) -> None:
        self._controller = BaseController(self)
        self._seeds = seeds
        super().__init__()


Language()
