from flask import Blueprint
from astro import to_json
from astro.user.models.user import User
from astro.base.controllers.base import BaseController

user = Blueprint("user", __name__)


@user.route("/create", methods=["POST"])
def create():
    return to_json(BaseController(User()).create())


@user.route("/get/all", methods=["GET"])
def get_all():
    return to_json(BaseController(User()).get_all())


@user.route("/get", methods=["GET"])
def get():
    return to_json(BaseController(User()).get())


@user.route("/delete/all", methods=["DELETE"])
def delete_all():
    return to_json(BaseController(User()).delete_all())


@user.route("/delete", methods=["DELETE"])
def delete():
    return to_json(BaseController(User()).delete())


@user.route("/update/all", methods=["PATCH"])
def update():
    return to_json(BaseController(User()).update_all())


@user.route("/update", methods=["PATCH"])
def update_all():
    return to_json(BaseController(User()).update())
