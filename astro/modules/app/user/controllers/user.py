from flask import request
from astro.modules.app.base.controllers.base import BaseController
from astro.modules.app.user.models.user import User


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
        id = request.args.get("id")
        user = User().get(id)
        return user.comments
