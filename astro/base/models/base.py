from faker import Faker
from astro import db
from flask import request
from astro.base.models.crud import CRUD
from astro.log.models.console_log import ConsoleLog
from astro.utils.models.utils import Utils


class Base(CRUD, Utils):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String())
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return str(self.__dict__)

    def create(self, **kwargs):
        record = super().create(json=kwargs)
        if record:
            return self.get(record.id)
        else:
            return None

    def get_all(self, order_by=None):
        records = super().get_all(order_by=order_by)
        if records:
            json = {
                "action": "get",
                "status": "successful",
                "message": f"{len(records)} records retrieved.",
                "class_name": self.__class__.__name__,
                "ip_address": request.remote_addr
            }
            ConsoleLog().log_info(json)
        return super().get_all(order_by=order_by)

    def get(self, id=None):
        record = super().get(id=id)
        if record:
            json = {
                "action": "get",
                "status": "successful",
                "message": f"Record #{record.id} retrieved.",
                "class_name": self.__class__.__name__,
                "ip_address": request.remote_addr,
                "record_id": record.id
            }
            # ConsoleLog().log_info(json)
        return super().get(id=id)

    def update(self, **kwargs):
        record = super().update(json=kwargs)
        if record:
            json = {
                "action": "update",
                "status": "successful",
                "message": f"Record #{record.id} updated.",
                "class_name": self.__class__.__name__,
                "ip_address": request.remote_addr,
                "record_id": record.id
            }
        ConsoleLog().log_info(json)
        return super().get(record.id)

    def update_all(self, **kwargs):
        return super().update_all(json=kwargs)

    def delete(self, id=None):
        record = super().delete(id=id)
        if record:
            json = {
                "action": "delete",
                "status": "successful",
                "message": f"Record #{record.id} deleted.",
                "class_name": self.__class__.__name__,
                "ip_address": request.remote_addr,
                "record_id": record.id
            }
            ConsoleLog().log_info(json)
        return None

    def delete_all(self):
        return super().delete_all()

    def seed(self, seeds):
        for seed in seeds:
            self.create(json=seed)
        return self.get_all()

    def factory(self):
        return None

    def factory_create(self, count):
        if self.factory():
            for i in range(int(count)):
                json = self.factory()
                self.create(json=json)
            return self.get_all()
        else:
            return None
