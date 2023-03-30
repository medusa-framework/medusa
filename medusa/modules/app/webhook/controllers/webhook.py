from flask import request
from medusa.modules.app.base.controllers.base import BaseController


class WebhookController(BaseController):
    """
    Represents a controller for handling webhooks. Inherits from BaseController.
    """

    def webhook(self):
        """
        Handles the webhook.

        Returns:
            dict: The request of the webhook.
        """
        new_model = self.model.__class__()
        new_model.request = request.form
        return new_model.webhook()
