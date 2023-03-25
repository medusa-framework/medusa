from flask import request
from flask_login import current_user


class BaseController():
    def __init__(self, model) -> None:
        self.model = model

    def create(self):
        json = request.json
        json["user_id"] = 1
        # if not json.get("user_id") and current_user.is_authenticated:
        #     json["user_id"] = current_user.id
        return self.model.create(**json)

    def get_all(self):
        return self.model.get_all()

    def get(self):
        id = request.args.get("id")
        return self.model.get(id)

    def delete_all(self):
        return self.model.delete_all()

    def delete(self):
        id = request.args.get("id")
        return self.model.delete(id)

    def update_all(self):
        json = request.json
        return self.model.update_all(json=json)

    def update(self):
        json = request.json
        id = request.args.get("id")
        json["id"] = id
        return self.model.update(json=json)

    def factory(self):
        count = request.args.get("count")
        return self.model.factory_create(count)

    def seed(self):
        return self.model.seed(self.model._seeds)
