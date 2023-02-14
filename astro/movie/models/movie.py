from astro import db
from astro.base.models.base import Base
from astro.genre.models.genre import Genre
from astro.language.models.language import Language
from astro.person.models.person import Person
from astro.tmdb.models.tmdb import TMDB
import tmdbsimple


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


class Movie(db.Model, Base, TMDB):
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

    def __init__(self) -> None:
        self.tmdb_model = tmdbsimple.Movies
        self.type = "movie"
        super().__init__()

    def tmdb_import(self, tmdb_object):
        record = super().tmdb_import(tmdb_object)
        for genre in tmdb_object.genres:
            genre_record = Genre().query.filter_by(id=genre.get("id")).first()
            if genre_record:
                record.movie_genres.append(genre_record)
        for language in tmdb_object.spoken_languages:
            language_record = Language().query.filter_by(
                iso_639_1=language.get("iso_639_1")).first()
            if language_record:
                record.movie_spoken_languages.append(language_record)
        self.import_people(record, tmdb_object)
        db.session.commit()
        return self.query.order_by(
            self.__class__.created_at.desc()).first()

    def import_person(self, json, record, type):
        tmdb_person = Person().select(json.get("id"))
        person_record = Person().create(json=tmdb_person)
        if person_record:
            if type == "cast":
                record.movie_cast.append(person_record)
            elif type == "crew":
                record.movie_crew.append(person_record)
        return record

    def import_people(self, record, movie_object):
        credits = movie_object.credits()
        for cast in credits.get("cast"):
            record = self.import_person(
                cast, record, "cast")
        for crew in credits.get("crew"):
            record = self.import_person(
                crew, record, "crew")
