from flask import current_app
from config.system import db
from modules.app.base.models.base import BaseModel


class Email(BaseModel, db.Model):
    subject = db.Column(db.String(255))
    recipients = db.Column(db.Text())
    body = db.Column(db.Text())
    html = db.Column(db.Text())
    sender = db.Column(
        db.String(255), default=current_app.config.get("MAIL_DEFAULT_SENDER"))
    cc = db.Column(db.Text())
    bcc = db.Column(db.Text())
    reply_to = db.Column(
        db.String(255), default=current_app.config.get("MAIL_DEFAULT_SENDER"))
    charset = db.Column(db.String(255), default="utf-8")
    sent = db.Column(db.Boolean, default=False)
    # attachments = db.Column(db.String(255))
    # extra_headers = db.Column(db.String(255))
    # mail_options = db.Column(db.String(255))
    # rcpt_options = db.Column(db.String(255))

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
