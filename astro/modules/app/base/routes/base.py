from flask import current_app, Blueprint
from flask_login import login_required
from astro.modules.app.base.controllers.base import BaseController
from astro.modules.app.utils.functions.utils import to_json


class BaseRoute:
    def __init__(self) -> None:
        self._name = self.__class__.__name__.lower()
        self._import_name = __name__
        self._blueprint = self.blueprint()
        self.routes()
        if not current_app.blueprints.get(self._name):
            current_app.register_blueprint(self._blueprint)

    def blueprint(self):
        return Blueprint(
            name=self._name,
            import_name=self._import_name,
            url_prefix="/api/" + self._name
        )

    def routes(self):
        @self._blueprint.route('/', methods=["GET"])
        def get():
            return to_json(BaseController(self.model()).get())

        @ self._blueprint.route('/all', methods=["GET"])
        def get_all():
            return to_json(BaseController(self.model()).get_all())

        @ self._blueprint.route('/', methods=["POST"])
        @ login_required
        def create():
            return to_json(BaseController(self.model()).create())

        @ self._blueprint.route('/', methods=["PATCH"])
        @ login_required
        def update():
            return to_json(BaseController(self.model()).update())

        @ self._blueprint.route('/all', methods=["PATCH"])
        @ login_required
        def update_all():
            return to_json(BaseController(self.model()).update_all())

        @ self._blueprint.route('/', methods=["DELETE"])
        @ login_required
        def delete():
            return to_json(BaseController(self.model()).delete())

        @ self._blueprint.route('/all', methods=["DELETE"])
        @ login_required
        def delete_all():
            return to_json(BaseController(self.model()).delete_all())

        @ self._blueprint.route('/factory', methods=["POST"])
        def factory():
            return to_json(BaseController(self.model()).factory())

        @ self._blueprint.route('/seed', methods=["POST"])
        def seed():
            return to_json(BaseController(self.model()).seed())
