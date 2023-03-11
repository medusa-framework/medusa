from flask import request
from astro.modules.app.base.controllers.base import BaseController


class UserController(BaseController):
    def login(self):
        return self.model.login()

    def current(self):
        return self.model.current()

    def logout(self):
        return self.model.logout()

    def register(self):
        return self.model.register()

    def comments(self):
        id = request.args.get("id")
        user = self.model.get(id)
        return user.comments
