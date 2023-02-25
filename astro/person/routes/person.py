from flask import Blueprint
from flask_login import login_required
from astro.utils.functions.utils import to_json
from astro.person.models.person import Person
from astro.base.controllers.base import BaseController
from astro.person.controllers.person import PersonController

person = Blueprint("person", __name__)


@person.route("/create", methods=["POST"])
@login_required
def create():
    return to_json(BaseController(Person()).create())


@person.route("/search", methods=["POST"])
def search():
    return to_json(PersonController().search())


@person.route("/select", methods=["POST"])
def select():
    return to_json(PersonController().select())


@person.route("/tmdb/import", methods=["POST"])
@login_required
def tmdb_import():
    return to_json(PersonController().tmdb_import())


@person.route("/get/all", methods=["GET"])
def get_all():
    return to_json(BaseController(Person()).get_all())


@person.route("/get", methods=["GET"])
def get():
    return to_json(BaseController(Person()).get())


@person.route("/delete/all", methods=["DELETE"])
@login_required
def delete_all():
    return to_json(BaseController(Person()).delete_all())


@person.route("/delete", methods=["DELETE"])
@login_required
def delete():
    return to_json(BaseController(Person()).delete())


@person.route("/update/all", methods=["PATCH"])
@login_required
def update():
    return to_json(BaseController(Person()).update_all())


@person.route("/update", methods=["PATCH"])
@login_required
def update_all():
    return to_json(BaseController(Person()).update())
