from astro.base.controllers.base import BaseController
from astro.user.models.user import User


class UserController(BaseController):

    def login(self):
        return User().login()

    def current(self):
        return User().current()

    def logout(self):
        return User().logout()

    def register(self):
        return User().register()

    def comments(self):
        user = User().get()
        return user.comments
