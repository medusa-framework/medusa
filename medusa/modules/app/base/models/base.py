from medusa import db
from medusa.modules.app.base.models.crud import CRUD
from medusa.modules.app.base.routes.base import BaseRoute


class Base(BaseRoute, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String())
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self) -> None:
        self._seeds = None
        super().__init__()

    def __repr__(self) -> str:
        return str(self.__dict__)

    def model(self):
        return self.__class__()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def get_all(self, order_by=None):
        return super().get_all(order_by=order_by)

    def get(self, id=None):
        return super().get(id=id)

    def update(self, **kwargs):
        return super().update(**kwargs)

    def update_all(self, **kwargs):
        return super().update_all(**kwargs)

    def delete(self, id=None):
        return super().delete(id=id)

    def delete_all(self):
        return super().delete_all()

    def seed(self):
        if not self.get_all():
            for seed in self._seeds:
                self.create(**seed)

    def factory(self):
        return None

    def factory_create(self, count):
        if self.factory():
            for i in range(int(count)):
                json = self.factory()
                self.create(**json)
            return self.get_all()
        else:
            return None


Base()
