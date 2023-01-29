from flask import Blueprint
from astro.base.controllers.base import BaseController
from astro.comment.models.comment import Comment
from astro import to_json

comment = Blueprint("comment", __name__)


@comment.route("/create", methods=["POST"])
def create():
    return to_json(BaseController(Comment()).create())


@comment.route("/get/all", methods=["GET"])
def get_all():
    return to_json(BaseController(Comment()).get_all())


@comment.route("/get", methods=["GET"])
def get():
    return to_json(BaseController(Comment()).get())


@comment.route("/delete/all", methods=["DELETE"])
def delete_all():
    return to_json(BaseController(Comment()).delete_all())


@comment.route("/delete", methods=["DELETE"])
def delete():
    return to_json(BaseController(Comment()).delete())


@comment.route("/update/all", methods=["PATCH"])
def update():
    return to_json(BaseController(Comment()).update_all())


@comment.route("/update", methods=["PATCH"])
def update_all():
    return to_json(BaseController(Comment()).update())
