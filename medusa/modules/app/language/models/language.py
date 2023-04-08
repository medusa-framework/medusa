from medusa import db
from medusa.modules.app.base.controllers.base import BaseController
from medusa.modules.app.base.models.base import Base
from medusa.modules.app.language.seeders.language import languages as seeds


class Language(Base, db.Model):
    """
    Model representing a language.

    Attributes:
        name (db.Column): A string column to store the name of the language.
        iso_639_1 (db.Column): A string column to store the iso_639_1 of the language.
        english_name (db.Column): A string column to store the English name of the language.
    """
    name = db.Column(db.String(50))
    iso_639_1 = db.Column(db.String(2))
    english_name = db.Column(db.String(50))

    def __init__(self) -> None:
        """
        Initialize a Language instance.
        """
        self._controller = BaseController(self)
        self._seeds = seeds
        super().__init__()


Language()
