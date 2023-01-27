from flask import Blueprint
from astro.comment.controllers.comment import CommentController

comment = Blueprint("comment", __name__)


@comment.route("/comment/create", methods=["POST"])
def create():
    return CommentController().create()


@comment.route("/comment/get/all", methods=["GET"])
def get_all():
    return CommentController().get_all()


@comment.route("/comment/get", methods=["GET"])
def get():
    return CommentController().get()


@comment.route("/comment/delete/all", methods=["DELETE"])
def delete_all():
    return CommentController().delete_all()


@comment.route("/comment/delete", methods=["DELETE"])
def delete():
    return CommentController().delete()


@comment.route("/comment/update/all", methods=["PATCH"])
def update():
    return CommentController().update_all()


@comment.route("/comment/update", methods=["PATCH"])
def update_all():
    return CommentController().update()
