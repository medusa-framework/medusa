from flask import request
from medusa.modules.app.base.controllers.base import BaseController


class UserController(BaseController):
    def login(self):
        json = request.json
        return self.model.login(**json)

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

    def delete_user_comments(self):
        comments = self.comments()
        return self.model.delete_user_comments(comments)

    def notifications(self):
        id = request.args.get("id")
        user = self.model.get(id)
        return user.notifications
