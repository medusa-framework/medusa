from medusa.modules.app.base.routes.base import BaseRoute
from medusa.modules.app.utils.functions.utils import to_json


class WebhookRoute(BaseRoute):
    """
    Represents a webhook route. Inherits from BaseRoute.
    """

    def routes(self):
        """
        Sets up the webhook route.

        Returns:
            function: The webhook route function.
        """
        @self._blueprint.route('/webhook', methods=["POST"])
        def webhook():
            """
            Retrieves the webhook request.

            Returns:
                dict: The request of the webhook.
            """
            return to_json(self._controller.webhook())

        return super().routes()
