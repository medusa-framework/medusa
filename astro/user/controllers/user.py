from astro.user.models.user import User
from astro import to_json


class UserController:

    def create(self):
        return to_json(User().create(
            username="georgegeorgegeorgegeorgegeorgegeorge",
            password="george2",
            email="george3"
        ))

    def get_all(self):
        return to_json(User().get_all())

    def get(self):
        return to_json(User().get())

    def delete_all(self):
        return to_json(User().delete_all())

    def delete(self):
        return to_json(User().delete())

    def update_all(self):
        return to_json(User().update_all(
            username="john",
            password="john2",
            email="john3"
        ))

    def update(self):
        return to_json(User().update(
            username="paul",
            password="paul2",
            email="paul3"
        ))
