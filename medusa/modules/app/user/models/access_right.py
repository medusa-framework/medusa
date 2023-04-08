from faker import Faker
from medusa.modules.app.base.controllers.base import BaseController
from medusa.modules.app.base.models.base import Base
from medusa.modules.app.user.seeders.access_right import access_rights as seeds
from medusa import db


class AccessRight(Base, db.Model):
    """Class representing an access right.

    Attributes:
        name (str): Name of the access right.
    """
    name = db.Column(db.String(50))

    def __init__(self) -> None:
        """Initializes a new instance of AccessRight.

        This constructor initializes a BaseController instance and a seeds object.
        """
        self._controller = BaseController(self)
        self._seeds = seeds
        super().__init__()

    def factory(self):
        """Creates a new AccessRight instance.

        Returns:
            dict: A dictionary containing the name of the access right.
        """
        faker = Faker()
        name = faker.word()
        json = {"name": name}
        return json


AccessRight()
