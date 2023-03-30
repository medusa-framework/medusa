from medusa.modules.app.base.models.base import Base
from medusa.modules.app.webhook.controllers.webhook import WebhookController
from medusa.modules.app.webhook.routes.webhook import WebhookRoute


class Webhook(Base, WebhookRoute):
    """
    Represents a webhook. Inherits from Base and WebhookRoute.
    """

    def __init__(self):
        """
        Constructor for the Webhook class.
        """
        self._controller = WebhookController(self)
        super().__init__()

    def webhook(self):
        """
        Retrieves the request of the webhook.

        Returns:
            dict: The request of the webhook.
        """
        return self.request


Webhook()
