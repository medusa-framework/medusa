from astro.person.models.person import Person
from flask import request
from astro import validate_int
import tmdbsimple


class PersonController:

    def create(self):
        return Person().create()

    def get_all(self):
        return Person().get_all()

    def get(self):
        return Person().get()

    def delete_all(self):
        return Person().delete_all()

    def delete(self):
        return Person().delete()

    def update_all(self):
        return Person().update_all()

    def update(self):
        return Person().update()

    def select(self):
        id = request.args.get("id")
        id = validate_int(id)
        try:
            return Person().select(id).info()
        except:
            return None

    def search(self):
        query = request.json.get("name")
        return Person().search(query=query)

    def tmdb_import(self):
        id = request.args.get("id")
        id = validate_int(id)
        return Person().tmdb_import(tmdbsimple.People(id))
