from astro import db, tmdb
from astro.base.models.base import Base
from flask import request


class Person(db.Model, Base):
    birthday = db.Column(db.String)
    known_for_department = db.Column(db.String)
    deathday = db.Column(db.String)
    tmdb_id = db.Column(db.Integer)
    name = db.Column(db.String)
    # also_known_as = db.relationship("AlsoKnownAs", backref="person", lazy=True)
    # gender = db.Column(db.Integer, db.ForeignKey("gender"))
    biography = db.Column(db.String)
    popularity = db.column(db.Float)
    place_of_birth = db.Column(db.String)
    profile_path = db.Column(db.String)
    adult = db.Column(db.Boolean)
    imdb_id = db.Column(db.String)
    homepage = db.Column(db.String)
    # TODO: external ids and credits

    def select(self):
        tmdb_id = self.validate_int(request.args.get("tmdb_id"))
        if tmdb_id:
            try:
                person = tmdb.People(request.args.get("tmdb_id")).info()
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
            person["tmdb_id"] = person.get("id")
            person["id"] = None
            if self.check_duplicate(tmdb_id=person.get("tmdb_id")):
                return None
            else:
                person_record = self.create(json=person)
                db.session.commit()
                return person_record
        else:
            print(
                f"ASTRO: {self.__class__.__name__} record not imported.\n \n")
            return None
