from faker import Faker
from medusa import db
from medusa.modules.app.base.controllers.base import BaseController
from medusa.modules.app.base.models.base import Base
from flask_login import current_user


class Message(Base):
    """Class representing a message.

    Attributes:
        message (str): The message content.
        user_id (int): ID of the user who sent the message.
    """
    message = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self) -> None:
        """Initializes a new instance of Message.

        This constructor initializes a BaseController instance.
        """
        self._controller = BaseController(self)
        super().__init__()

    def factory(self):
        """Creates a new Message instance.

        Returns:
            dict: A dictionary containing the user ID and message content.
        """
        json = {
            "user_id": current_user.id,
            "message": Faker().sentence(),
        }
        return json


Message()
