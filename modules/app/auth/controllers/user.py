from modules.app.base.controllers.base import BaseController


class UserController(BaseController):
    def controller_login(self, **request_json):
        return self.model_login(**request_json)

    def controller_logout(self):
        return self.model_logout()

    def controller_current(self):
        return self.model_current()

    def controller_comments(self, **request_args):
        return self.model_comments(**request_args)
