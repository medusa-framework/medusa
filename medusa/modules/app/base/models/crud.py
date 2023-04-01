from datetime import datetime
from uuid import uuid4
from medusa import db
from medusa.modules.app.utils.functions.utils import validate_int, kwargs_get


class CRUD:
    """
    Base class for database models with basic CRUD (Create, Read, Update, Delete) operations.
    """

    def create(self, **kwargs):
        """
        Creates a new record in the database.

        Args:
            **kwargs: The keyword arguments to use for creating the record.

        Returns:
            The created record.
        """
        model = self.__class__()
        model.uuid = str(uuid4())
        model.created_at = datetime.now()
        model.bind_attributes(**kwargs)
        record = self.check_duplicate(model)
        if not record:
            db.session.add(model)
            db.session.commit()
            record = model.query.order_by(
                model.__class__.created_at.desc()).first()
            return record
        else:
            return record

    def bind_attributes(self, **kwargs):
        """
        Binds keyword arguments to the database record attributes.

        Args:
            **kwargs: The keyword arguments to bind to the record.
        """
        self.updated_at = datetime.now()
        for arg in kwargs:
            if not arg.startswith("_"):
                setattr(self, arg, kwargs.get(arg))

    def get_all(self, order_by=None):
        """
        Retrieves all records from the database.

        Args:
            order_by (optional): The order in which to retrieve the records.

        Returns:
            A list of all records in the database.
        """
        records = self.query.all()
        if order_by:
            records = self.query.order_by(order_by).filter_by().all()
        else:
            records = self.query.filter_by().all()
        if records:
            return records
        else:
            return None

    def get(self, **kwargs):
        """
        Retrieve records from the database that match the specified filter criteria.

        Args:
            **kwargs: Filter criteria to apply to the query. Each keyword argument corresponds
            to a column in the database table.

        Returns:
            A list of records that match the specified filter criteria.
        """
        records = self.query.filter_by(**kwargs).all()
        if not records:
            return None
        return records

    def update(self, **kwargs):
        """
        Updates a record in the database.

        Args:
            **kwargs: The keyword arguments to use for updating the record.

        Returns:
            The updated record.
        """
        id = validate_int(kwargs.get("id"))
        record = self.query.filter_by(id=id).first()
        if record:
            record.bind_attributes(**kwargs)
            db.session.commit()
            return self.query.order_by(self.__class__.updated_at.desc()).first()
        else:
            return None

    def update_all(self, **kwargs):
        """
        Updates all records in the database.

        Args:
            **kwargs: The keyword arguments to use for updating the records.

        Returns:
            The updated records.
        """
        records = self.get_all()
        if not records:
            return None
        for record in records:
            kwargs["id"] = record.id
            record.update(**kwargs)
        return self.get_all(order_by="updated_at")

    def delete(self, id):
        """
        Deletes a record from the database by ID.

        Args:
            id: The ID of the record to delete.

        Returns:
            The deleted record.
        """
        id = validate_int(id)
        record = self.query.filter_by(id=id).first()
        if not record == None:
            record.updated_at = datetime.now()
            temp_record = record
            db.session.delete(record)
            db.session.commit()
            return temp_record
        else:
            return None

    def delete_all(self):
        """
        Delete all records from the database.
        Returns:
          The deleted records.
        """
        records = self.get_all()
        if records == None:
            return None
        for record in records:
            record.delete(record.id)
        return None

    def check_duplicate(self, model):
        """
        Checks if a record with the same ID or ISO code already exists in the database.

        Args:
            model: The model to check for duplicates.

        Returns:
            The existing record, or False if no record exists.
        """
        if model.__dict__.get("iso_639_1", False):
            record = self.query.filter_by(
                iso_639_1=model.iso_639_1).first()
        else:
            record = self.query.filter_by(id=model.id).first()
        if record:
            return record
        return False
