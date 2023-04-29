from modules.app.base.factories.factory import BaseFactory


class UserFactory(BaseFactory):
    def __init__(self) -> None:
        """
        Initializes a UserFactory instance.
        """
        super().__init__()

    def factory(self) -> dict:
        """
        Creates a user dictionary with generated data.

        Returns:
            A dictionary representing a user with generated data.
        """
        return {
            "username": self.generate_username(),
            "email": self.generate_email(),
            "password": "medusa",
            "first_name": self.generate_first_name(),
            "last_name": self.generate_last_name(),
            "display_name": self.generate_username(),
            "phone": self.generate_phone()
        }