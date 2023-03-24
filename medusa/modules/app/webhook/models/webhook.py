from medusa.modules.app.base.models.base import Base
from medusa.modules.app.webhook.controllers.webhook import WebhookController
from medusa.modules.app.webhook.routes.webhook import WebhookRoute


class Webhook(Base, WebhookRoute):

    def __init__(self):
        self._controller = WebhookController(self)
        super().__init__()

    def webhook(self):
        return self.request


Webhook()
