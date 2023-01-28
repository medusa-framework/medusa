from flask import Blueprint
from astro.user.controllers.user import UserController

user1 = Blueprint("user", __name__)


@user1.route("/create", methods=["POST"])
def create():
    return UserController().create()


@user1.route("/get/all", methods=["GET"])
def get_all():
    return UserController().get_all()


@user1.route("/get", methods=["GET"])
def get():
    return UserController().get()


@user1.route("/delete/all", methods=["DELETE"])
def delete_all():
    return UserController().delete_all()


@user1.route("/delete", methods=["DELETE"])
def delete():
    return UserController().delete()


@user1.route("/update/all", methods=["PATCH"])
def update():
    return UserController().update_all()


@user1.route("/update", methods=["PATCH"])
def update_all():
    return UserController().update()
