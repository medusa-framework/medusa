from flask import Blueprint
from flask_login import login_required
from astro import to_json
from astro.movie.models.movie import Movie
from astro.base.controllers.base import BaseController
from astro.movie.controllers.movie import MovieController

movie = Blueprint("movie", __name__)


@movie.route("/create", methods=["POST"])
@login_required
def create():
    return to_json(BaseController(Movie()).create())


@movie.route("/search", methods=["POST"])
def search():
    return to_json(MovieController().search())


@movie.route("/select", methods=["POST"])
def select():
    return to_json(MovieController().select())


@movie.route("/credits", methods=["POST"])
def credits():
    return to_json(MovieController().credits())


@movie.route("/tmdb/import", methods=["POST"])
@login_required
def tmdb_import():
    return to_json(MovieController().tmdb_import())


@movie.route("/get/all", methods=["GET"])
def get_all():
    return to_json(BaseController(Movie()).get_all())


@movie.route("/get", methods=["GET"])
def get():
    return to_json(BaseController(Movie()).get())


@movie.route("/delete/all", methods=["DELETE"])
@login_required
def delete_all():
    return to_json(BaseController(Movie()).delete_all())


@movie.route("/delete", methods=["DELETE"])
@login_required
def delete():
    return to_json(BaseController(Movie()).delete())


@movie.route("/update/all", methods=["PATCH"])
@login_required
def update():
    return to_json(BaseController(Movie()).update_all())


@movie.route("/update", methods=["PATCH"])
@login_required
def update_all():
    return to_json(BaseController(Movie()).update())
