from flask_login import current_user
from modules.app.base.models.base import BaseModel
from config.system import db


class Comment(BaseModel, db.Model):
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), default=1)

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def model_create(self, **kwargs):
        if not kwargs.get("user_id") and current_user:
            kwargs["user_id"] = current_user
        return super().model_create(**kwargs)
