from flask import Blueprint
from astro.movie.controllers.movie import MovieController

movie = Blueprint("movie", __name__)


@movie.route("/movie/create", methods=["POST"])
def create():
    return MovieController().create()


@movie.route("/movie/get/all", methods=["GET"])
def get_all():
    return MovieController().get_all()


@movie.route("/movie/get", methods=["GET"])
def get():
    return MovieController().get()


@movie.route("/movie/delete/all", methods=["DELETE"])
def delete_all():
    return MovieController().delete_all()


@movie.route("/movie/delete", methods=["DELETE"])
def delete():
    return MovieController().delete()


@movie.route("/movie/update/all", methods=["PATCH"])
def update():
    return MovieController().update_all()


@movie.route("/movie/update", methods=["PATCH"])
def update_all():
    return MovieController().update()
