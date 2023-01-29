from flask import Blueprint
from astro import to_json
from astro.movie.models.movie import Movie
from astro.base.controllers.base import BaseController

movie = Blueprint("movie", __name__)


@movie.route("/create", methods=["POST"])
def create():
    return to_json(BaseController(Movie()).create())


@movie.route("/get/all", methods=["GET"])
def get_all():
    return to_json(BaseController(Movie()).get_all())


@movie.route("/get", methods=["GET"])
def get():
    return to_json(BaseController(Movie()).get())


@movie.route("/delete/all", methods=["DELETE"])
def delete_all():
    return to_json(BaseController(Movie()).delete_all())


@movie.route("/delete", methods=["DELETE"])
def delete():
    return to_json(BaseController(Movie()).delete())


@movie.route("/update/all", methods=["PATCH"])
def update():
    return to_json(BaseController(Movie()).update_all())


@movie.route("/update", methods=["PATCH"])
def update_all():
    return to_json(BaseController(Movie()).update())
