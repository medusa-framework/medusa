from flask import request
from modules.base.controllers.base import BaseController


class UserController(BaseController):
    def controller_login(self, **kwargs):
        return self.model_login(**kwargs)

    def controller_logout(self):
        return self.model_logout()
