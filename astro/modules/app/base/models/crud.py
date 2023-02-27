from datetime import datetime
from uuid import uuid4
from astro import db
from astro.modules.app.utils.functions.utils import validate_int, kwargs_get


class CRUD:

    def create(self, **kwargs):
        model = self.__class__()
        model.uuid = str(uuid4())
        model.created_at = datetime.now()
        model.bind_attributes(kwargs)
        record = self.check_duplicate(model)
        if not record:
            db.session.add(model)
            db.session.commit()
            record = model.query.order_by(
                model.__class__.created_at.desc()).first()
            return record
        else:
            return record

    def get_all(self, order_by=None):
        records = self.query.all()
        if order_by:
            records = self.query.order_by(order_by).filter_by().all()
        else:
            records = self.query.filter_by().all()
        if not records == []:
            return records
        else:
            return None

    def get(self, id):
        if validate_int(id):
            return self.query.filter_by(id=id).first()
        else:
            return None

    def update(self, **kwargs):
        id = kwargs_get(kwargs, "id")
        record = self.query.filter_by(id=id).first()
        if not record == None:
            record.updated_at = datetime.now()
            record.bind_attributes(kwargs)
            db.session.commit()
            return self.query.order_by(self.__class__.updated_at.desc()).first()
        else:
            return None

    def update_all(self, **kwargs):
        records = self.get_all()
        if records == []:
            return None
        for record in records:
            kwargs["id"] = record.id
            record.update(json=kwargs)
        return self.get_all(order_by="updated_at")

    def delete(self, id):
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
        records = self.get_all()
        if records == None:
            return None
        temp_records = records
        for record in records:
            record.delete()
        return temp_records

    def check_duplicate(self, model):
        if model.__dict__.get("iso_639_1", False):
            record = self.query.filter_by(
                iso_639_1=model.iso_639_1).first()
        else:
            record = self.query.filter_by(id=model.id).first()
        if record:
            return record
        return False

    def bind_attributes(self, json):
        self.updated_at = datetime.now()
        if "json" in json.keys():
            return self.bind_attributes(json.get("json"))
        else:
            for arg in json:
                setattr(self, arg, json.get(arg))
