from flask import request
from flask_login import login_required
from medusa.modules.app.base.routes.base import BaseRoute
from medusa.modules.app.utils.functions.utils import to_json


class UserRoute(BaseRoute):
    """
    Route for handling user-related requests.
    Inherits from BaseRoute.
    """

    def routes(self):
        @self._blueprint.route('/register', methods=["POST"])
        def register():
            """
            Register a new user.

            Returns:
                str: The registration status.
            """
            return to_json(self._controller.register())

        @self._blueprint.route('/login', methods=["POST"])
        def login():
            """
            Log in a user.

            Returns:
                str: The login status.
            """
            return to_json(self._controller.login())

        @self._blueprint.route('/logout', methods=["POST"])
        # @login_required
        def logout():
            """
            Log out the current user.

            Returns:
                str: The logout status.
            """
            return to_json(self._controller.logout())

        @self._blueprint.route('/current', methods=["GET"])
        # @login_required
        def current():
            """
            Get information about the current logged-in user.

            Returns:
                str: The user information.
            """
            return to_json(self._controller.current())

        @self._blueprint.route('/comments', methods=["GET"])
        # @login_required
        def comments():
            """
            Get comments made by a user.

            Returns:
                str: The user's comments.
            """
            return to_json(self._controller.comments())

        @self._blueprint.route('/notifications', methods=["GET"])
        # @login_required
        def notifications():
            """
            Get notifications for a user.

            Returns:
                str: The user's notifications.
            """
            return to_json(self._controller.notifications())

        @self._blueprint.route('/delete_user_comments', methods=["DELETE"])
        # @login_required
        def delete_user_comments():
            """
            Delete all comments made by a user.

            Returns:
                str: The deletion status.
            """
            return to_json(self._controller.delete_user_comments())

        return super().routes()
