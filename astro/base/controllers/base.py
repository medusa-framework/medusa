from astro import to_json
from astro.base.models.base import Base


class BaseController():

    def __init__(self, model) -> None:
        self.model = model

    def create(self):
        return self.model.create()

    def get_all(self):
        return self.model.get_all()

    def get(self):
        return self.model.get()

    def delete_all(self):
        return self.model.delete_all()

    def delete(self):
        return self.model.delete()

    def update_all(self):
        return self.model.update_all()

    def update(self):
        return self.model.update()
