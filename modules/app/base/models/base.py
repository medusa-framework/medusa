from flask import current_app
from sqlalchemy import or_
from modules.app.base.controllers.base import BaseController
from modules.app.base.routes.base import BaseRoute
from utils.printable import Printable
from utils.init_models import init_modules
from config.system import db
from datetime import datetime
import uuid
from config import logger
from faker import Faker
import random



class BaseModel(BaseRoute, BaseController):
    def generate_uuid(self):
        return str(uuid.uuid4())

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), default=generate_uuid)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


    def __init__(self, **kwargs) -> None:
        self.set_attributes(self, kwargs)
        super().__init__()

    def set_attributes(self, obj, kwargs):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                modules = init_modules(current_app.config.get("MODULES_DIR"))
                for model in modules:
                    if model._name == value.get("model").lower():
                        records = model.filter_by_any(value.get("ids")).all()
                setattr(obj, key, records)
            else:
                setattr(obj, "updated_at", datetime.now())
                setattr(obj, key, value)

    def filter_by_any(self, args):
        query = db.session.query(self.__class__)
        if not args:
            return query
        filters = []
        if isinstance(args, dict):
            for k, v in args.items():
                if isinstance(v, str) and k == "id":
                    if v.isdigit():
                        v = int(v)
                    else:
                        continue
                if isinstance(v, int):
                    filters.append(getattr(self.__class__, k) == v)
                else:
                    filters.append(getattr(self.__class__, k).ilike(f"%{v}%"))
        elif isinstance(args, list):
            for v in args:
                if isinstance(v, int):
                    filters.append(getattr(self.__class__, "id") == v)
        if filters:
            return query.filter(or_(*filters))
        else:
            return query

    def model_create(self, **request_json):
        record = self.__class__(**request_json)
        try:
            db.session.add(record)
            db.session.commit()
        except Exception as e:
            self.log_record("POST", f"Record create failed. {type(e)} {e.orig}", record)
            return None
        self.log_record("POST", "Record created", record)
        return self.query.filter_by(id=record.id).first()

    def model_get(self, **request_args):
        for key, value in request_args.items():
            if key == "id":
                request_args["id"] = int(request_args.get("id"))
        records = self.filter_by_any(request_args).all()
        self.log_record_multi("GET", "Records retrieved", records)
        return records

    def model_update(self, request_args=None, **request_json):
        updated_at = []
        for record in self.filter_by_any(request_args).all():
            self.set_attributes(record, request_json)
            updated_at.append(record.updated_at)
        try:
            db.session.commit()
        except Exception as e:
            self.log_record("PATCH", f"Record update failed. {type(e)} {e.orig}", record)
            return None
        if not updated_at:
            return []
        records = self.query.filter(
            self.__class__.updated_at.between(updated_at[0], updated_at[-1])
        ).all()
        self.log_record_multi("PATCH", "Records updated", records)
        return records

    def model_delete(self, **request_args):
        records = self.filter_by_any(request_args).all()
        try:
            for record in records:
                db.session.delete(record)
            db.session.commit()
        except Exception as e:
            self.log_record("DELETE", f"Record delete failed. {type(e)} {e.orig}", record)
            return None
        self.log_record_multi("DELETE", "Records deleted", records)
        return records
    
    def model_factory(self):
        faker = Faker()
        table = self.__class__.__table__
        kwargs = {}
        for column in table.columns:
            if not column.name.startswith('_'):
                if column.name == "id" or column.name == "uuid":
                    continue
            col_type = column.type.__class__.__name__
            if col_type == "String":
                word_count = random.randint(1, 10)
                words = faker.words(nb=word_count)
                kwargs[column.name] = " ".join(words)[:column.type.length]
            elif col_type == "DateTime":
                kwargs[column.name] = datetime.now()
            elif col_type == "Integer":
                kwargs[column.name] = random.randint(1, 2000)
        return "ok"

    def log_record_multi(self, request_type, message, records):
        id_list = []
        for record in records:
            id_list.append(record.id)
        logger.debug(
            "%s %s %s (id:%s)",
            self.__class__.__name__.upper(),
            request_type,
            message,
            id_list,
        )

    def log_record(self, request_type, message, record):
        logger.debug(
            "%s %s %s (id:%s)",
            self.__class__.__name__.upper(),
            request_type,
            message,
            record.id,
        )
