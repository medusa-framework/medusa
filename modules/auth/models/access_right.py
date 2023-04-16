from config.app import db
from modules.base.models.base import BaseModel


class AccessRight(BaseModel, db.Model):
    name = db.Column(db.String(255))
    model = db.Column(db.String(255))

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
