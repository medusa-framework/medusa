from flask import request
from medusa.modules.app.base.controllers.base import BaseController


class WebhookController(BaseController):
    def webhook(self):
        new_model = self.model.__class__()
        new_model.request = request.form
        return new_model.webhook()
