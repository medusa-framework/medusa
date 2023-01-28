from flask import Blueprint
from astro.movie.controllers.movie import MovieController

movie = Blueprint("movie", __name__)


@movie.route("/create", methods=["POST"])
def create():
    return MovieController().create()


@movie.route("/get/all", methods=["GET"])
def get_all():
    return MovieController().get_all()


@movie.route("/get", methods=["GET"])
def get():
    return MovieController().get()


@movie.route("/delete/all", methods=["DELETE"])
def delete_all():
    return MovieController().delete_all()


@movie.route("/delete", methods=["DELETE"])
def delete():
    return MovieController().delete()


@movie.route("/update/all", methods=["PATCH"])
def update():
    return MovieController().update_all()


@movie.route("/update", methods=["PATCH"])
def update_all():
    return MovieController().update()
