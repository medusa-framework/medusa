from config.app import db
from modules.app.auth.models.access_right import AccessRight
from modules.app.base.models.base import BaseModel


access_group_access_right = db.Table(
    "access_group_access_right",
    db.Column("access_right_id", db.Integer, db.ForeignKey(
        "access_right.id"), primary_key=True),
    db.Column("access_group_id", db.Integer, db.ForeignKey(
        "access_group.id"), primary_key=True)
)


class AccessGroup(BaseModel, db.Model):
    name = db.Column(db.String(255))
    access_group_access_right = db.relationship(
        "AccessRight",
        secondary=access_group_access_right,
        lazy="subquery",
        backref=db.backref("access_group", lazy=True)
    )

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
