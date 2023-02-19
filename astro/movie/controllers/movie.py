from astro.base.controllers.base import BaseController
from astro.movie.models.movie import Movie
from astro import validate_int
from flask import request
import tmdbsimple


class MovieController(BaseController):
    def select(self):
        id = request.args.get("id")
        id = validate_int(id)
        try:
            return Movie().select(id).info()
        except:
            return None

    def credits(self):
        try:
            return Movie().credits()
        except:
            return None

    def search(self):
        query = request.json.get("title")
        year = request.json.get("year")
        return Movie().search(query=query, year=year)

    def tmdb_import(self):
        id = request.args.get("id")
        id = validate_int(id)
        return Movie().tmdb_import(tmdbsimple.Movies(id))
