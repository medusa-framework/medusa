from medusa import db
from medusa.modules.app.user.models.message import Message


class Comment(Message, db.Model):
    message = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


Comment()
