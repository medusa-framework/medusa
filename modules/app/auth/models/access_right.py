from config.packages import db
from modules.app.base.models.base import BaseModel


class AccessRight(BaseModel, db.Model):
    name = db.Column(db.String(255))
    model = db.Column(db.String(255))
    default = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
