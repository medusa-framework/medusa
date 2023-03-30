from flask import current_app, Blueprint
from flask_login import login_required
from medusa.modules.app.base.controllers.base import BaseController
from medusa.modules.app.utils.functions.utils import to_json


class BaseRoute:
    """
    Base route class for handling CRUD routes for a model.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of BaseRoute.
        """
        self._name = self.__class__.__name__.lower()
        self._import_name = __name__
        self._blueprint = self.blueprint()
        self.routes()
        if not current_app.blueprints.get(self._name):
            current_app.register_blueprint(self._blueprint)

    def blueprint(self):
        """
        Creates a Flask blueprint for the route.

        Returns:
            The blueprint for the route.
        """
        return Blueprint(
            name=self._name,
            import_name=self._import_name,
            url_prefix="/api/" + self._name
        )

    def routes(self):
        """
        Defines the routes for the blueprint.
        """
        @self._blueprint.route('/', methods=["GET"])
        def get():
            """
            Retrieves a record from the database by ID.

            Returns:
                The retrieved record.
            """
            return to_json(BaseController(self.model()).get())

        @self._blueprint.route('/all', methods=["GET"])
        def get_all():
            """
            Retrieves all records from the database.

            Returns:
                A list of all records in the database.
            """
            return to_json(BaseController(self.model()).get_all())

        @self._blueprint.route('/', methods=["POST"])
        # @login_required
        def create():
            """
            Creates a new record in the database.

            Returns:
                The created record.
            """
            return to_json(BaseController(self.model()).create())

        @self._blueprint.route('/', methods=["PATCH"])
        # @login_required
        def update():
            """
            Updates a record in the database by ID.

            Returns:
                The updated record.
            """
            return to_json(BaseController(self.model()).update())

        @self._blueprint.route('/all', methods=["PATCH"])
        # @login_required
        def update_all():
            """
            Updates all records in the database.

            Returns:
                The updated records.
            """
            return to_json(BaseController(self.model()).update_all())

        @self._blueprint.route('/', methods=["DELETE"])
        # @login_required
        def delete():
            """
            Deletes a record from the database by ID.

            Returns:
                The deleted record.
            """
            return to_json(BaseController(self.model()).delete())

        @self._blueprint.route('/all', methods=["DELETE"])
        # @login_required
        def delete_all():
            """
            Deletes all records from the database.

            Returns:
                None
            """
            return to_json(BaseController(self.model()).delete_all())

        @self._blueprint.route('/factory', methods=["POST"])
        def factory():
            """
            Creates a certain number of new records in the database using a factory.

            Returns:
                The created records.
            """
            return to_json(BaseController(self.model()).factory())

        @self._blueprint.route('/seed', methods=["POST"])
        def seed():
            """
            Seeds the database with a set of predefined records.

            Returns:
                None
            """
            return to_json(BaseController(self.model()).seed())
