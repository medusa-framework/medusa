from astro.user.models.user import User1
from astro import to_json


class UserController:

    def create(self):
        return to_json(User1().create(
            username="georgegeorgegeorgegeorgegeorgegeorge",
            password="george2",
            email="george3"
        ))

    def get_all(self):
        return to_json(User1().get_all())

    def get(self):
        return to_json(User1().get())

    def delete_all(self):
        return to_json(User1().delete_all())

    def delete(self):
        return to_json(User1().delete())

    def update_all(self):
        return to_json(User1().update_all(username="john", password="john2", email="john3"))

    def update(self):
        return to_json(User1().update(username="paul", password="paul2", email="paul3"))
