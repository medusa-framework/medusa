from datetime import datetime
from uuid import uuid4
from medusa import db
from medusa.modules.app.utils.functions.utils import validate_int
import logging


class CRUD():
    """
    Base class for database models with basic CRUD (Create, Read, Update, Delete) operations.
    Creates loggers for werkzeug and medusa to split log files.
    """
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    werkzeug_logger = logging.getLogger('werkzeug')
    werkzeug_handler = logging.FileHandler("logs/werkzeug.log")
    werkzeug_handler.setLevel(logging.DEBUG)
    werkzeug_handler.setFormatter(formatter)
    werkzeug_logger.addHandler(werkzeug_handler)

    mds_logger = logging.getLogger('medusa')
    mds_handler = logging.FileHandler("logs/medusa.log")
    mds_handler.setLevel(logging.DEBUG)
    mds_handler.setFormatter(formatter)
    mds_logger.addHandler(mds_handler)

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
            logging.info("[%s] [%s] Record %s created.",
                         self.__class__.__name__.upper(), "POST", record.id)
            return record
        else:
            logging.warning("[%s] [%s] Record %s already exists.",
                            self.__class__.__name__.upper(), "POST", record.id)
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
            logging.warning("[%s] [%s] No matching records found.",
                            self.__class__.__name__.upper(), "GET")
            return None
        else:
            logging.info("[%s] [%s] %s matching records found.",
                         self.__class__.__name__.upper(), "GET", len(records))
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
            logging.info("[%s] [%s] Record %s updated.",
                         self.__class__.__name__.upper(), "PATCH", id)
            return self.query.order_by(self.__class__.updated_at.desc()).first()
        else:
            logging.warning("[%s] [%s] No matching records found.",
                            self.__class__.__name__.upper(), "PATCH")
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
            logging.warning("[%s] [%s] No matching records found.",
                            self.__class__.__name__.upper(), "PATCH")
            return None
        for record in records:
            kwargs["id"] = record.id
            record.update(**kwargs)
            logging.info("[%s] [%s] %s matching records updated.",
                         self.__class__.__name__.upper(), "PATCH", len(records))
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
            logging.info("[%s] [%s] Record %s deleted.",
                         self.__class__.__name__.upper(), "DELETE", id)
            return temp_record
        else:
            logging.warning("[%s] [%s] No matching records found.",
                            self.__class__.__name__.upper(), "DELETE")
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
        logging.info("[%s] [%s] %s matching records deleted.",
                     self.__class__.__name__.upper(), "DELETE", len(records))
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
