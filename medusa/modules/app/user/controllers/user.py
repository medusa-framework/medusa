from flask import request
from medusa.modules.app.base.controllers.base import BaseController


class UserController(BaseController):
    """
    Controller for handling user-related operations.
    Inherits from BaseController.
    """

    def login(self):
        """
        Log in a user using the provided credentials.

        Returns:
            str: The login status.
        """
        json = request.json
        return self.model.login(**json)

    def current(self):
        """
        Get information about the current logged-in user.

        Returns:
            str: The user information.
        """
        return self.model.current()

    def logout(self):
        """
        Log out the current user.

        Returns:
            str: The logout status.
        """
        return self.model.logout()

    def register(self):
        """
        Register a new user.

        Returns:
            str: The registration status.
        """
        return self.model.register()

    def comments(self):
        """
        Get comments made by a user.

        Returns:
            str: The user's comments.
        """
        id = request.args.get("id")
        user = self.model.get(id)
        return user.comments

    def delete_user_comments(self):
        """
        Delete all comments made by a user.

        Returns:
            str: The deletion status.
        """
        comments = self.comments()
        return self.model.delete_user_comments(comments)

    def notifications(self):
        """
        Get notifications for a user.

        Returns:
            str: The user's notifications.
        """
        id = request.args.get("id")
        user = self.model.get(id)
        return user.notifications
