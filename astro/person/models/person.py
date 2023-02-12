from astro import db, tmdb
from astro.base.models.base import Base
from flask import request

# TODO: set up relationships and pivot tables


class Person(db.Model, Base):
    birthday = db.Column(db.String)
    known_for_department = db.Column(db.String)
    deathday = db.Column(db.String)
    name = db.Column(db.String)
    # also_known_as = db.relationship("AlsoKnownAs", backref="person", lazy=True)
    # gender = db.Column(db.Integer, db.ForeignKey("gender"))
    biography = db.Column(db.String)
    popularity = db.Column(db.Float)
    place_of_birth = db.Column(db.String)
    profile_path = db.Column(db.String)
    adult = db.Column(db.Boolean)
    imdb_id = db.Column(db.String)
    homepage = db.Column(db.String)
    # TODO: external ids and credits

    def select(self):
        id = self.validate_int(request.args.get("id"))
        if id:
            try:
                person = tmdb.People(request.args.get("id")).info()
                return person
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
        name = request.json.get("name")
        response = search.person(query=name)
        if response.get("results"):
            return response.get("results")
        else:
            print(
                f"ASTRO: {self.__class__.__name__} record not found.\n \n")
            return None

    def tmdb_import(self):
        person = self.select()
        if person:
            person_record = self.create(json=person)
            db.session.commit()
            return person_record
        else:
            print(
                f"ASTRO: {self.__class__.__name__} record not imported.\n \n")
            return None
