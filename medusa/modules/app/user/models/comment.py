from medusa import db
from medusa.modules.app.user.models.message import Message


class Comment(Message, db.Model):
    """
    Class representing a comment. Inherits from Message.
    """
    pass


Comment()
