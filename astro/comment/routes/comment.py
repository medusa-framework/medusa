from flask import Blueprint
from flask_login import login_required
from astro.base.controllers.base import BaseController
from astro.comment.models.comment import Comment
from astro import to_json

comment = Blueprint("comment", __name__)


@comment.route("/create", methods=["POST"])
@login_required
def create():
    return to_json(BaseController(Comment()).create())


@comment.route("/get/all", methods=["GET"])
def get_all():
    return to_json(BaseController(Comment()).get_all())


@comment.route("/get", methods=["GET"])
def get():
    return to_json(BaseController(Comment()).get())


@comment.route("/delete/all", methods=["DELETE"])
@login_required
def delete_all():
    return to_json(BaseController(Comment()).delete_all())


@comment.route("/delete", methods=["DELETE"])
@login_required
def delete():
    return to_json(BaseController(Comment()).delete())


@comment.route("/update/all", methods=["PATCH"])
@login_required
def update():
    return to_json(BaseController(Comment()).update_all())


@comment.route("/update", methods=["PATCH"])
@login_required
def update_all():
    return to_json(BaseController(Comment()).update())
