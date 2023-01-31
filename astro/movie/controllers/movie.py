from astro.movie.models.movie import Movie


class MovieController:

    def create(self):
        return Movie().create(
            title="pulp fiction",
            duration=120,
            director="footguy32"
        )

    def get_all(self):
        return Movie().get_all()

    def get(self):
        return Movie().get()

    def delete_all(self):
        return Movie().delete_all()

    def delete(self):
        return Movie().delete()

    def update_all(self):
        return Movie().update_all(
            title="kill bill",
            duration=92,
            director="qdawg11"
        )

    def update(self):
        return Movie().update(
            title="reservoir dogs",
            duration=260,
            director="tarantino"
        )

    def select(self):
        return Movie().select()

    def search(self):
        return Movie().search()

    def tmdb_import(self):
        return Movie().tmdb_import()
