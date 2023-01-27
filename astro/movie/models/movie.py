from astro import db
from flask import request


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    duration = db.Column(db.Integer)
    director = db.Column(db.String(120))

    def __init__(self, title=None, duration=None, director=None):
        self.title = title
        self.director = director
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"

    def create(self, title=None, duration=None, director=None):
        self.title = title
        self.director = director
        self.duration = duration
        db.session.add(self)
        db.session.commit()
        return self.query.order_by(Movie.id.desc()).first()

    def get_all(self):
        return self.query.order_by("id").all()

    def get(self):
        id = request.args.get("id")
        return self.query.filter_by(id=id).first()

    def update(self, title=None, duration=None, director=None):
        movie = self.get()
        movie.title = title
        movie.director = director
        movie.duration = duration
        db.session.commit()
        return self.query.filter_by(id=movie.id).first()

    def update_all(self, title=None, duration=None, director=None):
        movies = self.query.all()
        for movie in movies:
            movie.title = title
            movie.director = director
            movie.duration = duration
            db.session.commit()
        return self.query.order_by("id").all()

    def delete(self):
        movie = self.get()
        temp_movie = self.get()
        db.session.delete(movie)
        db.session.commit()
        return temp_movie

    def delete_all(self):
        # get all movies
        movies = self.query.all()
        temp_movies = self.query.all()
        # loop through movies
        print(movies)
        for movie in movies:
            db.session.delete(movie)
            db.session.commit()
        # delete records
        return temp_movies
