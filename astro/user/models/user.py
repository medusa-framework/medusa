from astro import db
from flask import request


class User1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String())
    email = db.Column(db.String(120))

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"

    def create(self, username=None, password=None, email=None):
        self.username = username
        self.email = email
        self.password = password
        db.session.add(self)
        db.session.commit()
        return self.query.filter_by(email=email).first()

    def get_all(self):
        return self.query.order_by("id").all()

    def get(self):
        id = request.args.get("id")
        return self.query.filter_by(id=id).first()

    def update(self, username=None, password=None, email=None):
        user = self.get()
        user.username = username
        user.email = email
        user.password = password
        db.session.commit()
        return self.query.filter_by(id=user.id).first()

    def update_all(self, username=None, password=None, email=None):
        users = self.query.all()
        for user in users:
            user.username = username
            user.email = email
            user.password = password
            db.session.commit()
        return self.query.order_by("id").all()

    def delete(self):
        user = self.get()
        temp_user = self.get()
        db.session.delete(user)
        db.session.commit()
        return temp_user

    def delete_all(self):
        # get all users
        users = self.query.all()
        temp_users = self.query.all()
        # loop through users
        print(users)
        for user in users:
            db.session.delete(user)
            db.session.commit()
        # delete records
        return temp_users
