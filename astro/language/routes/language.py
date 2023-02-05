from flask import Blueprint
from flask_login import login_required
from astro import to_json
from astro.language.models.language import Language
from astro.base.controllers.base import BaseController
from astro.language.controllers.language import LanguageController

language = Blueprint("language", __name__)


@language.route("/create", methods=["POST"])
@login_required
def create():
    return to_json(BaseController(Language()).create())


@language.route("/import", methods=["POST"])
@login_required
def tmdb_import():
    return to_json(LanguageController().tmdb_import())


@language.route("/get/all", methods=["GET"])
def get_all():
    return to_json(BaseController(Language()).get_all())


@language.route("/get", methods=["GET"])
def get():
    return to_json(BaseController(Language()).get())


@language.route("/delete/all", methods=["DELETE"])
@login_required
def delete_all():
    return to_json(BaseController(Language()).delete_all())


@language.route("/delete", methods=["DELETE"])
@login_required
def delete():
    return to_json(BaseController(Language()).delete())


@language.route("/update/all", methods=["PATCH"])
@login_required
def update():
    return to_json(BaseController(Language()).update_all())


@language.route("/update", methods=["PATCH"])
@login_required
def update_all():
    return to_json(BaseController(Language()).update())
