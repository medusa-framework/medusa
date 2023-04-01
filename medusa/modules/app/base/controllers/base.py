from flask import request
from flask_login import current_user


class BaseController():
    """
    Base controller class for handling CRUD operations for a model.
    """

    def __init__(self, model) -> None:
        """Initialize a BaseController instance.

        Args:
            model: the database model to use for CRUD operations.
        """
        self.model = model

    def create(self) -> object:
        """Create a new record in the database.

        Returns:
            The created record.
        """
        json = request.json
        if not json.get("user_id") and current_user.is_authenticated:
            json["user_id"] = current_user.id
        json["request_type"] = request.method
        return self.model.create(**json)

    def get_all(self) -> list:
        """Retrieve all records from the database.

        Returns:
            A list of all records in the database.
        """
        return self.model.get_all()

    def get(self) -> object:
        """Retrieve a record from the database.

        Returns:
            The retrieved record.
        """
        query_params = request.args.to_dict()
        return self.model.get(**query_params)

    def delete_all(self) -> None:
        """Delete all records from the database."""
        return self.model.delete_all()

    def delete(self) -> object:
        """Delete a record from the database by ID.

        Returns:
            The deleted record.
        """
        id = request.args.get("id")
        return self.model.delete(id)

    def update_all(self) -> list:
        """Update all records in the database.

        Returns:
            The updated records.
        """
        json = request.json
        return self.model.update_all(**json)

    def update(self) -> object:
        """Update a record in the database by ID.

        Returns:
            The updated record.
        """
        json = request.json
        json["id"] = request.args.get("id")
        json["request_type"] = request.method
        return self.model.update(**json)

    def factory(self) -> list:
        """Create a certain number of new records in the database using a factory.

        Returns:
            The created records.
        """
        count = request.args.get("count")
        return self.model.factory_create(count)

    def seed(self) -> None:
        """Seed the database with a set of predefined records."""
        return self.model.seed(self.model._seeds)
