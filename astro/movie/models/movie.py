from astro import db, tmdb
from astro.base.models.base import Base
from flask import request
from astro.genre.models.genre import Genre
from astro.language.models.language import Language
from astro.person.models.person import Person


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

movie_crew = db.Table(
    "movie_crew",
    db.Column("person_id", db.Integer, db.ForeignKey(
        "person.id"), primary_key=True),
    db.Column("movie_id", db.Integer, db.ForeignKey(
        "movie.id"), primary_key=True)
)

movie_cast = db.Table(
    "movie_cast",
    db.Column("person_id", db.Integer, db.ForeignKey(
        "person.id"), primary_key=True),
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
    movie_genres = db.relationship(
        "Genre",
        secondary=movie_genres,
        lazy="subquery",
        backref=db.backref("movies", lazy=True)
    )
    movie_spoken_languages = db.relationship(
        "Language",
        secondary=movie_spoken_languages,
        lazy="subquery",
        backref=db.backref("movies", lazy=True)
    )
    movie_crew = db.relationship(
        "Person",
        secondary=movie_crew,
        lazy="subquery",
        backref=db.backref("movies", lazy=True)
    )
    movie_cast = db.relationship(
        "Person",
        secondary=movie_cast,
        lazy="subquery",
        backref=db.backref("movies2", lazy=True)
    )

    def select(self):
        id = self.validate_int(request.args.get("id"))
        if id:
            try:
                movie = tmdb.Movies(request.args.get("id")).info()
                return movie
            except:
                print(
                    f"ASTRO: {self.__class__.__name__} record not found.\n \n")
                return None
        else:
            print(
                f"ASTRO: {self.__class__.__name__} record not found.\n \n")
            return None

    def credits(self):
        id = self.validate_int(request.args.get("id"))
        if id:
            try:
                movie = tmdb.Movies(request.args.get("id")).credits()
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
        credits = self.credits()
        if movie:
            movie_record = self.create(json=movie)
            for genre in movie.get("genres"):
                genre_record = Genre().query.filter_by(id=genre.get("id")).first()
                if genre_record:
                    movie_record.movie_genres.append(genre_record)
                    db.session.commit()
            for language in movie.get("spoken_languages"):
                language_record = Language().query.filter_by(
                    iso_639_1=language.get("iso_639_1")).first()
                movie_record.movie_spoken_languages.append(language_record)
                db.session.commit()
            for crew in credits.get("crew"):
                person_record = Person().create(json=crew)
                if person_record:
                    movie_record.movie_crew.append(person_record)
                    db.session.commit()
            for cast in credits.get("cast"):
                person_record = Person().create(json=cast)
                if person_record:
                    movie_record.movie_cast.append(person_record)
                    db.session.commit()
            return movie_record

        else:
            print(
                f"ASTRO: {self.__class__.__name__} record not imported.\n \n")
            return None
