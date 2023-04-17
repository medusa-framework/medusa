from config.packages import db
from modules.app.base.models.base import BaseModel


class Language(BaseModel, db.Model):
    name = db.Column(db.String(255))
    english_name = db.Column(db.String(255))
    iso_639_1 = db.Column(db.String(2))

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
