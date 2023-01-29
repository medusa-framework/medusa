from flask import Blueprint
from astro.user.controllers.user import UserController

user = Blueprint("user", __name__)


@user.route("/create", methods=["POST"])
def create():
    return UserController().create()


@user.route("/get/all", methods=["GET"])
def get_all():
    return UserController().get_all()


@user.route("/get", methods=["GET"])
def get():
    return UserController().get()


@user.route("/delete/all", methods=["DELETE"])
def delete_all():
    return UserController().delete_all()


@user.route("/delete", methods=["DELETE"])
def delete():
    return UserController().delete()


@user.route("/update/all", methods=["PATCH"])
def update():
    return UserController().update_all()


@user.route("/update", methods=["PATCH"])
def update_all():
    return UserController().update()
