from modules.app.base.models.email import BaseEmail
from flask import current_app, render_template


class RegisterEmail(BaseEmail):
    def __init__(self, recipients, **kwargs) -> None:
        """
        Initializes a RegisterEmail instance. Should return super init call.

        Args:
            recipients: A list of email recipients.
            **kwargs: Additional keyword arguments coming from the controller to be used in the email template.

        Attributes:
            app_name: Current app name.
            subject: Email subject line.
            html: HTML template to be rendered.

        Returns:
            The init function of BaseEmail through a super call.
        """
        app_name = current_app.config.get('APP_NAME')
        subject = f"Welcome to {app_name}, {kwargs.get('username')}"
        html = render_template(
            "register.html", app_name=app_name, kwargs=kwargs)
        super().__init__(recipients=recipients, subject=subject, html=html)
