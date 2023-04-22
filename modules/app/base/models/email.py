import logging
from flask import current_app
from flask_mail import Message
from modules.app.email.email import Email
from config.system import mail, db


class BaseEmail(Message):
    def __init__(self, recipients, **kwargs):
        setattr(self, "recipients", recipients)
        for key, value in kwargs.items():
            setattr(self, key, value)
        if not kwargs.get("sender"):
            setattr(
                self, "sender",
                (
                    current_app.config.get("MAIL_DISPLAY_NAME"),
                    current_app.config.get("MAIL_DEFAULT_SENDER")
                )
            )
        super().__init__(**vars(self))

    def send_email(self):
        email = Email().model_create(**vars(self))
        try:
            mail.send(self)
            email.sent = True
            db.session.commit()
            self.log_email("Email sent successfully", email)
        except Exception as e:
            self.log_email("Unable to send email.", email)

    def log_email(self, message: str, email: object):
        logging.warn(
            "[EMAIL] %s (id:%s)",
            message,
            email.id,
        )
