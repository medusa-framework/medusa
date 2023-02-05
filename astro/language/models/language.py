from astro import db
from astro.base.models.base import Base
import requests
from flask import current_app


class Language(db.Model, Base):
    name = db.Column(db.String)
    iso_639_1 = db.Column(db.String)
    english_name = db.Column(db.String)

    def tmdb_import(self):
        url = f"https://api.themoviedb.org/3/configuration/languages?api_key={current_app.config.get('TMDB_API_KEY')}&language=en-US"
        languages = requests.get(url)
        count = 0
        for language in languages.json():
            if self.check_duplicate(iso_639_1=language.get("iso_639_1")):
                continue
            else:
                Language().create(json=language)
                count += 1
        print(
            f"ASTRO: {count} {self.__class__.__name__} records imported.\n \n")
        return self.get_all()
