from medusa import db
from medusa.modules.app.base.models.crud import CRUD
from medusa.modules.app.base.routes.base import BaseRoute


class Base(BaseRoute, CRUD):
    """
    Base class for database models with basic CRUD operations.
    """
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self) -> None:
        """
        Initialize the Base class.
        """
        self._seeds = None
        super().__init__()

    def __repr__(self) -> str:
        """
        Return a string representation of the Base class instance.
        """
        return str(self.__dict__)

    def model(self):
        """
        Create a new instance of the Base class.
        """
        return self.__class__()

    def create(self, **kwargs):
        """
        Create a new record in the database.

        Args:
            **kwargs: the keyword arguments to use for creating the record.

        Returns:
            The created record.
        """
        return super().create(**kwargs)

    def get_all(self, order_by=None):
        """Retrieve all records from the database.

        Args:
            order_by: the order in which to retrieve the records.

        Returns:
            A list of all records in the database.
        """
        return super().get_all(order_by=order_by)

    def get(self, **kwargs):
        """Retrieve a record from the database by ID.

        Args:
            id: the ID of the record to retrieve.

        Returns:
            The retrieved record.
        """
        return super().get(**kwargs)

    def update(self, **kwargs):
        """Update a record in the database.

        Args:
            **kwargs: the keyword arguments to use for updating the record.

        Returns:
            The updated record.
        """
        return super().update(**kwargs)

    def update_all(self, **kwargs):
        """Update all records in the database.

        Args:
            **kwargs: the keyword arguments to use for updating the records.

        Returns:
            The updated records.
        """
        return super().update_all(**kwargs)

    def delete(self, id=None):
        """Delete a record from the database by ID.

        Args:
            id: the ID of the record to delete.

        Returns:
            The deleted record.
        """
        return super().delete(id=id)

    def delete_all(self):
        """Delete all records from the database.

        Returns:
            The deleted records.
        """
        return super().delete_all()

    def seed(self):
        """
        Seed the database with default records.
        """
        if not self.get_all():
            for seed in self._seeds:
                self.create(**seed)

    def factory(self):
        """
        Create a new record using factory pattern.
        """
        return None

    def factory_create(self, count):
        """Create multiple records using factory pattern.

        Args:
            count: the number of records to create.

        Returns:
            A list of created records.
        """
        if self.factory():
            for i in range(int(count)):
                json = self.factory()
                self.create(**json)
            return self.get_all()
        else:
            return None


Base()
