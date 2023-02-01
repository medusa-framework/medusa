from astro import db
from astro.base.models.base import Base
import requests
from flask import current_app


class Genre(db.Model, Base):
    name = db.Column(db.String)
    tmdb_id = db.Column(db.Integer)

    def tmdb_import(self):
        # get request to find genres
        url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={current_app.config.get('TMDB_API_KEY')}&language=en-US"
        genres = requests.get(url)
        count = 0
        # loop through ids
        for genre in genres.json().get("genres"):
            # properly assign ids
            genre["tmdb_id"] = genre.get("id")
            genre["id"] = None
            if self.check_duplicate(genre.get("tmdb_id")):
                continue
            else:
                Genre().create(json=genre)
                count += 1
        print(
            f"ASTRO: {count} {self.__class__.__name__} records imported.\n \n")
        return self.get_all()
