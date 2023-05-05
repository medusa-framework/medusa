from config.system import db
from modules.app.base.models.base import BaseModel


class AccessRight(BaseModel, db.Model):
    """
    Represents an access right in the system.
    
    Attributes:
            name (str): The name of the Access Right.
            model (str): The model that corresponds to the Access Right.
            default (bool): Default true/false value for the Access Right.
    """
    name = db.Column(db.String(255))
    model = db.Column(db.String(255))
    default = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs) -> None:
        """
        Initializes an AccessRight instance that takes in keyword arguments.

        Args:
            name: The name of the Access Right.
            model: The model that corresponds to the Access Right.
            default (optional): Default true/false value for the Access Right.
        """
        super().__init__(**kwargs)
