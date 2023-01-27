from astro.movie.models.movie import Movie
from astro import to_json


class MovieController:

    def create(self):
        return to_json(Movie().create(
            title="pulp fiction",
            duration=120,
            director="footguy32"
        ))

    def get_all(self):
        return to_json(Movie().get_all())

    def get(self):
        return to_json(Movie().get())

    def delete_all(self):
        return to_json(Movie().delete_all())

    def delete(self):
        return to_json(Movie().delete())

    def update_all(self):
        return to_json(Movie().update_all(
            title="kill bill",
            duration=92,
            director="qdawg11"
        ))

    def update(self):
        return to_json(Movie().update(
            title="reservoir dogs",
            duration=260,
            director="tarantino"
        ))
