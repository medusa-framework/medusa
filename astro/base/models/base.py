from datetime import datetime
from uuid import uuid4
from astro import db
from flask import request


class Base():
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String())
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return str(self.__dict__)

    def create(self, json=None, **kwargs):
        if not json:
            json = request.json
        self.uuid = str(uuid4())
        self.created_at = datetime.now()
        self.bind_attributes(json, kwargs)
        db.session.add(self)
        db.session.commit()
        record = self.query.order_by(self.__class__.created_at.desc()).first()
        print(
            f"ASTRO: {self.__class__.__name__} record # {record.id} added succesfully.\n \n")
        return record

    def get_all(self, attr=None, soft=False):
        records = self.query.all()
        if attr:
            records = self.query.order_by(attr).filter_by(deleted=soft).all()
        else:
            records = self.query.filter_by(deleted=soft).all()
        if not records == []:
            print(
                f"ASTRO: {self.__class__.__name__} records found: \n {records}.\n \n")
            return records
        else:
            print(
                f"ASTRO: {self.__class__.__name__} records not found.\n \n")
            return None

    def get(self, id=None):
        if self.id:
            return self
        if request.args and request.args.get("id"):
            id = self.validate_int(request.args.get("id"))
        if id:
            id = self.validate_int(id)
        if id:
            return self.query.filter_by(id=id, deleted=False).first()
        else:
            print(
                f"ASTRO: {self.__class__.__name__} record not found.\n \n")
            return None

    def update(self, json=None, id=None, **kwargs):
        if not json:
            json = request.json
        if self.id:
            id = self.id
        else:
            id = request.args.get('id')
        record = self.query.filter_by(id=id).first()
        if not record == None:
            record.updated_at = datetime.now()
            record.bind_attributes(json, kwargs)
            db.session.commit()
            print(
                f"ASTRO: {self.__class__.__name__} record # {record.id} updated succesfully.\n \n")
            return self.query.order_by(self.__class__.updated_at.desc()).first()
        else:
            print(
                f"ASTRO: {self.__class__.__name__} record id {request.args.get('id')} not found.\n \n")
            return None

    def update_all(self, json=None, **kwargs):
        if not json:
            json = request.json
        records = self.get_all()
        if records == []:
            return None
        for record in records:
            record.update(kwargs)
        return self.get_all(attr="updated_at")

    def bind_attributes(self, json=None, kwargs=None):
        self.updated_at = datetime.now()
        for arg in request.json:
            setattr(self, arg, request.json.get(arg))
        for arg in json:
            setattr(self, arg, json.get(arg))
        for arg in kwargs:
            setattr(self, arg, kwargs.get(arg))

    def delete(self, id=None, soft=True):
        if self.id:
            id = self.id
        else:
            id = request.args.get('id')
        record = self.query.filter_by(id=id).first()
        if not record == None:
            record.updated_at = datetime.now()
            temp_record = record
            if request.args.get("soft") == "0":
                soft = False
            if soft == True:
                record.deleted = True
            else:
                db.session.delete(record)
            db.session.commit()
            print(
                f"ASTRO: {self.__class__.__name__} record # {record.id} deleted succesfully.\n \n")
            return temp_record
        else:
            print(
                f"ASTRO: {self.__class__.__name__} record id {request.args.get('id')} not found.\n \n")
            return None

    def delete_all(self):
        records = self.get_all()
        if records == []:
            return None
        temp_records = records
        for record in records:
            record.delete()
        return temp_records

    def validate_int(self, id):
        if isinstance(id, str) and id.isdigit():
            return int(id)
        elif isinstance(id, int):
            return id
        else:
            return None

    def check_duplicate(self, tmdb_id):
        record = self.query.filter_by(tmdb_id=tmdb_id, deleted=False).first()
        if record:
            return True
        else:
            return False
