from sqlalchemy import or_
from modules.base.controllers.base import BaseController
from modules.base.routes.base import BaseRoute
from utils.printable import Printable
from config.app import db
from datetime import datetime
import uuid
import logging


class BaseModel(BaseRoute, BaseController):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs) -> None:
        self.set_attributes(self, kwargs)
        super().__init__()

    def set_attributes(self, obj, kwargs):
        for key, value in kwargs.items():
            setattr(obj, "updated_at", datetime.now())
            setattr(obj, key, value)

    def filter_by_any(self, args):
        query = db.session.query(self.__class__)
        filters = []
        for k, v in args.items():
            if isinstance(v, int):
                filters.append(getattr(self.__class__, k) == v)
            else:
                filters.append(getattr(self.__class__, k).ilike(f"%{v}%"))
        if filters:
            return query.filter(or_(*filters))
        else:
            return query

    def model_create(self, **kwargs):
        record = self.__class__(**kwargs)
        print(vars(record))
        db.session.add(record)
        db.session.commit()
        self.log_record("POST", "Record created", record)
        return self.query.filter_by(id=record.id).first()

    def model_get(self, **request_args):
        for key, value in request_args.items():
            if key == "id":
                request_args["id"] = int(request_args.get("id"))
        records = self.filter_by_any(request_args).all()
        self.log_record_multi("GET", "Records retrieved", records)
        # return "OK"
        return records

    def model_update(self, request_args=None, **kwargs):
        updated_at = []
        for record in self.filter_by_any(request_args).all():
            self.set_attributes(record, kwargs)
            updated_at.append(record.updated_at)
        db.session.commit()
        if not updated_at:
            return []
        records = self.query.filter(
            self.__class__.updated_at.between(updated_at[0], updated_at[-1])
        ).all()
        self.log_record_multi("PATCH", "Records updated", records)
        return records

    def model_delete(self, **request_args):
        records = self.filter_by_any(request_args).all()
        for record in self.filter_by_any(request_args):
            db.session.delete(record)
        db.session.commit()
        self.log_record_multi("DELETE", "Records deleted", records)
        return records

    def log_record_multi(self, request_type, message, records):
        id_list = []
        for record in records:
            id_list.append(record.id)
        logging.warn(
            "[%s] [%s] %s (id:%s)",
            self.__class__.__name__.upper(),
            request_type,
            message,
            id_list,
        )

    def log_record(self, request_type, message, record):
        logging.warn(
            "[%s] [%s] %s (id:%s)",
            self.__class__.__name__.upper(),
            request_type,
            message,
            record.id,
        )
