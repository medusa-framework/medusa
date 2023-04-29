from modules.app.base.controllers.base import BaseController


class UserController(BaseController):
    def controller_login(self, **request_json) -> object:
        """
        Controller method to handle User login requests that takes in request data in JSON format.

        Args:
            email: Email address of the User.
            password: Password of the User.

        Returns:
            The object record of the User that was logged in.
        """
        return self.model_login(**request_json)

    def controller_logout(self) -> object:
        """
        Controller method to handle User logout requests.

        Returns:
            The object record of the User that was logged out.
        """
        return self.model_logout()

    def controller_current(self) -> object:
        """
        Controller method to handle requests for the current User.

        Returns:
            The object record of the current authenticated User.
        """
        return self.model_current()

    def controller_comments(self, **request_args) -> list:
        """
        Controller method to handle requests for the current User's Comments that takes in request data. 
        If no arguments are given, all User Comments will be returned.
        
        Args:
            id (optional): The id of the User.

        Returns:
            List of object records of the current authenticated User's Comments.
        """
        return self.model_comments(**request_args)
