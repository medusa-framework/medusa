from astro import db, tmdb, to_json
from astro.base.models.base import Base
from flask import request
from astro.genre.models.genre import Genre
from astro.language.models.language import Language


movie_genres = db.Table(
    "movie_genres",
    db.Column("genre_id", db.Integer, db.ForeignKey(
        "genre.id"), primary_key=True),
    db.Column("movie_id", db.Integer, db.ForeignKey(
        "movie.id"), primary_key=True)
)

movie_spoken_languages = db.Table(
    "movie_spoken_languages",
    db.Column("language_id", db.Integer, db.ForeignKey(
        "language.id"), primary_key=True),
    db.Column("movie_id", db.Integer, db.ForeignKey(
        "movie.id"), primary_key=True)
)


class Movie(db.Model, Base):
    title = db.Column(db.String(128))
    overview = db.Column(db.String)
    adult = db.Column(db.Boolean)
    backdrop_path = db.Column(db.String)
    budget = db.Column(db.Integer)
    homepage = db.Column(db.String)
    imdb_id = db.Column(db.String)
    original_language = db.Column(db.String)
    original_title = db.Column(db.String)
    popularity = db.Column(db.Float)
    poster_path = db.Column(db.String)
    release_date = db.Column(db.String)
    revenue = db.Column(db.Integer)
    runtime = db.Column(db.Integer)
    status = db.Column(db.String)
    tagline = db.Column(db.String)
    tmdb_id = db.Column(db.Integer)
    movie_genres = db.relationship(
        "Genre",
        secondary=movie_genres,
        lazy="subquery",
        backref=db.backref("movies", lazy=True))
    movie_spoken_languages = db.relationship(
        "Language",
        secondary=movie_spoken_languages,
        lazy="subquery",
        backref=db.backref("movies", lazy=True)
    )

    def select(self):
        tmdb_id = self.validate_int(request.args.get("tmdb_id"))
        if tmdb_id:
            try:
                movie = tmdb.Movies(request.args.get("tmdb_id")).info()
                return movie
            except:
                print(
                    f"ASTRO: {self.__class__.__name__} record not found.\n \n")
                return None
        else:
            print(
                f"ASTRO: {self.__class__.__name__} record not found.\n \n")
            return None

    def search(self):
        search = tmdb.Search()
        title = request.json.get("title")
        year = request.json.get("year")
        response = search.movie(query=title, year=year)
        if response.get("results"):
            return response.get("results")
        else:
            print(
                f"ASTRO: {self.__class__.__name__} record not found.\n \n")
            return None

    def tmdb_import(self):
        movie = self.select()
        if movie:
            movie["tmdb_id"] = movie.get("id")
            movie["id"] = None
            if self.check_duplicate(tmdb_id=movie.get("tmdb_id")):
                return None
            else:
                movie_record = self.create(json=movie)
                for genre in movie.get("genres"):
                    genre_record = Genre().query.filter_by(tmdb_id=genre.get("id")).first()
                    movie_record.movie_genres.append(genre_record)
                    db.session.commit()
                for language in movie.get("spoken_languages"):
                    language_record = Language().query.filter_by(
                        iso_639_1=language.get("iso_639_1")).first()
                    movie_record.movie_spoken_languages.append(language_record)
                    db.session.commit()
                return movie_record
        else:
            print(
                f"ASTRO: {self.__class__.__name__} record not imported.\n \n")
            return None

    # def check_duplicate(self, tmdb_id):
    #     record = self.query.filter_by(tmdb_id=tmdb_id, deleted=False).first()
    #     if record:
    #         return True
    #     else:
    #         return False
