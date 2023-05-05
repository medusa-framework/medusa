from config.system import db
from modules.app.auth.models.access_right import AccessRight
from modules.app.base.models.base import BaseModel

"""
Defines a pivot table relationship between Access Groups and Access Rights.
"""
access_group_access_right = db.Table(
    "access_group_access_right",
    db.Column("access_right_id", db.Integer, db.ForeignKey(
        "access_right.id"), primary_key=True),
    db.Column("access_group_id", db.Integer, db.ForeignKey(
        "access_group.id"), primary_key=True)
)


class AccessGroup(BaseModel, db.Model):
    """
    Represents an Access Group.

    Attributes:
    name (str): The name of the Access Group.
    access_group_access_right (list[AccessRight]): The Access Groups associated with the User.
    """

    name = db.Column(db.String(255))
    access_group_access_right = db.relationship(
        "AccessRight",
        secondary=access_group_access_right,
        lazy="subquery",
        backref=db.backref("access_group", lazy=True)
    )

    def __init__(self, **kwargs) -> None:
        """
        Initializes an AccessGroup instance that takes in keyword arguments.
        Should return super init call.

        Args:
            name: The name of the Access Group.
            access_group_access_right = The list of Access Rights within an Access Group.
        """
        super().__init__(**kwargs)
