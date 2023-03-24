from medusa.modules.app.base.routes.base import BaseRoute
from medusa.modules.app.utils.functions.utils import to_json


class WebhookRoute(BaseRoute):
    def routes(self):
        @self._blueprint.route('/webhook', methods=["POST"])
        def webhook():
            return to_json(self._controller.webhook())

        return super().routes()
