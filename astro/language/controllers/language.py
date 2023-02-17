from astro.language.models.language import Language
from astro.language.seeders.language import languages


class LanguageController:

    def create(self):
        return Language().create()

    def get_all(self):
        return Language().get_all()

    def get(self):
        return Language().get()

    def delete_all(self):
        return Language().delete_all()

    def delete(self):
        return Language().delete()

    def update_all(self):
        return Language().update_all()

    def update(self):
        return Language().update()

    def select(self):
        return Language().select()

    def search(self):
        return Language().search()

    def seed(self):
        return Language().seed(languages)
