from astro.genre.models.genre import Genre
from astro.genre.seeders.genre import genres


class GenreController:

    def create(self):
        return Genre().create()

    def get_all(self):
        return Genre().get_all()

    def get(self):
        return Genre().get()

    def delete_all(self):
        return Genre().delete_all()

    def delete(self):
        return Genre().delete()

    def update_all(self):
        return Genre().update_all()

    def update(self):
        return Genre().update()

    def select(self):
        return Genre().select()

    def search(self):
        return Genre().search()

    def seed(self):
        return Genre().seed(genres)
