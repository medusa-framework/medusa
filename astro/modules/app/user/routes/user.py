from flask_login import login_required
from astro.modules.app.base.routes.base import BaseRoute
from astro.modules.app.utils.functions.utils import to_json


class UserRoute(BaseRoute):
    def routes(self):
        @self._blueprint.route('/register', methods=["POST"])
        def register():
            return to_json(self._controller.register())

        @self._blueprint.route('/login', methods=["POST"])
        def login():
            return to_json(self._controller.login())

        @self._blueprint.route('/logout', methods=["POST"])
        @login_required
        def logout():
            return to_json(self._controller.logout())

        @self._blueprint.route('/current', methods=["GET"])
        @login_required
        def current():
            return to_json(self._controller.current())

        return super().routes()
