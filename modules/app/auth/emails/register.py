from modules.app.base.models.email import BaseEmail
from flask import current_app, render_template


class RegisterEmail(BaseEmail):
    def __init__(self, recipients, **kwargs):
        app_name = current_app.config.get('APP_NAME')
        subject = f"Welcome to {app_name}, {kwargs.get('username')}"
        html = render_template(
            "register.html", app_name=app_name, kwargs=kwargs)
        super().__init__(recipients=recipients, subject=subject, html=html)
