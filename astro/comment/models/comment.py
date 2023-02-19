import random
from faker import Faker
from astro import db
from astro.base.models.base import Base
from flask_login import current_user
from astro.user.models.user import User


class Comment(db.Model, Base):
    message = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def create(self, **kwargs):
        if not kwargs.get("user_id"):
            kwargs["user_id"] = current_user.id
        return super().create(json=kwargs)

    def random_user_id(self, **kwargs):
        # get all users
        users = User().get_all()
        # create list of ids
        user_ids = []
        for user in users:
            user_ids.append(user.id)
        # pull random id from list
        user_id = random.choice(user_ids)
        return user_id

    def factory(self):
        faker = Faker()
        user_id = self.random_user_id()
        message = faker.sentence()
        json = {
            "user_id": user_id,
            "message": message,
        }
        return json
