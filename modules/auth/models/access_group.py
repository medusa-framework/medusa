from config.app import db
from modules.base.models.base import BaseModel


access_group_rights = db.Table(
    "access_group_rights",
    db.Column("access_right_id", db.Integer, db.ForeignKey(
        "access_right.id"), primary_key=True),
    db.Column("access_group_id", db.Integer, db.ForeignKey(
        "access_group.id"), primary_key=True)
)


class AccessGroup(BaseModel, db.Model):
    name = db.Column(db.String(255))

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
