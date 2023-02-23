from flask import Blueprint
from flask_login import login_required
from astro.utils.models.utils import Utils
from astro.user.models.user import User
from astro.base.controllers.base import BaseController
from astro.user.controllers.user import UserController
user = Blueprint("user", __name__)


@user.route("/create", methods=["POST"])
def create():
    return Utils().to_json(BaseController(User()).create())


@user.route("/register", methods=["POST"])
def register():
    return Utils().to_json(UserController(User()).register())


@user.route("/login", methods=["POST"])
def login():
    return Utils().to_json(UserController(User()).login())


@user.route("/logout", methods=["POST"])
def logout():
    return Utils().to_json(UserController(User()).logout())


@user.route("/factory", methods=["POST"])
def factory():
    return Utils().to_json(UserController(User()).factory())


@user.route("/current", methods=["GET"])
def current():
    return Utils().to_json(UserController(User()).current())


@user.route("/get/all", methods=["GET"])
def get_all():
    return Utils().to_json(BaseController(User()).get_all())


@user.route("/get", methods=["GET"])
def get():
    return Utils().to_json(BaseController(User()).get())


@user.route("/comments", methods=["GET"])
def comments():
    return Utils().to_json(UserController(User()).comments())


@user.route("/delete/all", methods=["DELETE"])
@login_required
def delete_all():
    return Utils().to_json(BaseController(User()).delete_all())


@user.route("/delete", methods=["DELETE"])
@login_required
def delete():
    return Utils().to_json(BaseController(User()).delete())


@user.route("/update/all", methods=["PATCH"])
@login_required
def update():
    return Utils().to_json(BaseController(User()).update_all())


@user.route("/update", methods=["PATCH"])
@login_required
def update_all():
    return Utils().to_json(BaseController(User()).update())
