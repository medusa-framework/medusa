from astro.user.models.user import User


class UserController:

    def login(self):
        return User().login()

    def current(self):
        return User().current()

    def logout(self):
        return User().logout()

    def register(self):
        return User().register()

    def comments(self):
        return User()._comments()
