from astro.movie.models.movie import Movie
from astro import tmdb, validate_int
from flask import request


class MovieController:

    def create(self):
        return Movie().create()

    def get_all(self):
        return Movie().get_all()

    def get(self):
        return Movie().get()

    def delete_all(self):
        return Movie().delete_all()

    def delete(self):
        return Movie().delete()

    def update_all(self):
        return Movie().update_all()

    def update(self):
        return Movie().update()

    def select(self):
        id = request.args.get("id")
        id = validate_int(id)
        return Movie().select(id)

    def credits(self):
        return Movie().credits()

    def search(self):
        return Movie().search()

    def tmdb_import(self):
        id = request.args.get("id")
        id = validate_int(id)
        return Movie().tmdb_import(tmdb.Movies(id))
