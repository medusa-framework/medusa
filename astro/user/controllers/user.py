from astro.user.models.user import User


class UserController:

    def create(self):
        return User().create(
            username="georgegeorgegeorgegeorgegeorgegeorge",
            password="george2",
            email="george3"
        )

    def get_all(self):
        return User().get_all()

    def get(self):
        return User().get()

    def delete_all(self):
        return User().delete_all()

    def delete(self):
        return User().delete()

    def update_all(self):
        return User().update_all(
            username="john",
            password="john2",
            email="john3"
        )

    def update(self):
        return User().update(
            username="paul",
            password="paul2",
            email="paul3"
        )
