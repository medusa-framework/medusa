from flask import current_app
import tmdbsimple


class TMDB():
    def __init__(self) -> None:
        tmdbsimple.API_KEY = current_app.config.get("TMDB_API_KEY")

    def tmdb_import(self, tmdb_object):
        record = self.create(json=tmdb_object.info())
        return record

    def select(self, id):
        try:
            info = self.tmdb_model(id).info()
            print("Success", id)
            return self.tmdb_model(id)
        except:
            print("Failed", id)
            return None

    def search(self, query=None, year=None):
        search = tmdbsimple.Search()
        if self.type == "movie":
            response = search.movie(query=query, year=year)
        elif self.type == "person":
            response = search.person(query=query)
        if response.get("results"):
            return response.get("results")
        else:
            print(
                f"ASTRO: {self.__class__.__name__} record not found.\n \n")
            return None
