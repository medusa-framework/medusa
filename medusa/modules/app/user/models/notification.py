from medusa import db
from medusa.modules.app.user.models.message import Message


class Notification(Message, db.Model):
    """
    Class representing a notification. Inherits from Message.

    Attributes:
        id (int): ID of the notification.
    """

    def get(self, id=None):
        """
        Retrieves a notification from the database.

        Args:
            id (int): ID of the notification to retrieve.

        Returns:
            dict: A dictionary containing the ID of the notification.
        """
        record = super().get(id)
        json = {"id": record.id}
        record.update(**json)
        return super().get(id)


Notification()
