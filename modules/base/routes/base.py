from flask import Blueprint, current_app, request
from utils.to_json import to_json


class BaseRoute():
    def __init__(self) -> None:
        self._name = self.__class__.__name__.lower()
        self._blueprint = self.blueprint()
        self.routes()
        if not current_app.blueprints.get(self._name):
            current_app.register_blueprint(self._blueprint)
        super().__init__()

    def blueprint(self):
        return Blueprint(
            name=self._name,
            import_name=__name__,
            url_prefix="/api/" + self._name
        )

    def routes(self):
        @self._blueprint.route('/', methods=["POST"])
        def route_create():
            return to_json(self.controller_create(**request.json))

        @self._blueprint.route('/', methods=["PATCH"])
        def route_update():
            return to_json(self.controller_update(request.args, **request.json))

        @self._blueprint.route('/', methods=["DELETE"])
        def route_delete():
            return to_json(self.controller_delete(**request.args))

        @self._blueprint.route('/', methods=["GET"])
        def route_get():
            return to_json(self.controller_get(**request.args))

        @self._blueprint.route('/factory', methods=["POST"])
        def route_factory():
            return to_json(self.controller_factory())
