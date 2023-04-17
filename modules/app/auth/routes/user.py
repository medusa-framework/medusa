from flask import request
from modules.app.base.routes.base import BaseRoute
from utils.to_json import to_json


class UserRoute(BaseRoute):
    def __init__(self) -> None:
        super().__init__()

    def routes(self):
        @self._blueprint.route('/login', methods=["POST"])
        def route_login():
            return to_json(self.controller_login(**request.json))

        @self._blueprint.route('/logout', methods=["POST"])
        def route_logout():
            return to_json(self.controller_logout())

        @self._blueprint.route('/current', methods=["POST"])
        def route_current():
            return to_json(self.controller_current())

        @self._blueprint.route('/comments', methods=["GET"])
        def route_comments():
            return to_json(self.controller_comments(**request.args))

        return super().routes()
