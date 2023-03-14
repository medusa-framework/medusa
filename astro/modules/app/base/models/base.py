from astro import db
from datetime import datetime
from astro.modules.app.base.models.crud import CRUD
from astro.modules.app.base.routes.base import BaseRoute
import json


def serialize(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return {k: v for k, v in obj.__dict__.items() if not k.startswith('_')}


def to_json(obj):
    json_str = json.dumps(obj, default=serialize)
    return json_str


class Base(BaseRoute, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String())
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return str(self.__dict__)

    def model(self):
        return self.__class__()

    def create(self, **kwargs):
        record = super().create(json=kwargs)
        if record:
            return self.get(record.id)
        else:
            return None

    def get_all(self, order_by=None):
        return super().get_all(order_by=order_by)

    def get(self, id=None):
        return super().get(id=id)

    def update(self, **kwargs):
        return super().update(json=kwargs)

    def update_all(self, **kwargs):
        return super().update_all(json=kwargs)

    def delete(self, id=None):
        return super().delete(id=id)

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


Base()
