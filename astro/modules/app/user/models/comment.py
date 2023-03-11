from astro import db
from astro.modules.app.user.models.message import Message


class Comment(Message, db.Model):
    pass


Comment()
