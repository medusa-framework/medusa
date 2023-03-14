from faker import Faker
from flask import request
from flask_login import login_user, current_user, logout_user
from astro import db, bcrypt, login_manager
from astro.modules.app.base.models.base import Base
from astro.modules.app.user.controllers.user import UserController
from flask_login import UserMixin
from astro.modules.app.user.routes.user import UserRoute
from astro.modules.app.user.seeders.user import users as seeds


class User(Base, UserRoute, db.Model, UserMixin):

    username = db.Column(db.String(128))
    password = db.Column(db.String())
    email = db.Column(db.String(120))
    comments = db.relationship("Comment", backref="user", lazy=True)
    notifications = db.relationship("Notification", backref="user", lazy=True)

    def __init__(self) -> None:
        self._controller = UserController(self)
        self._seeds = seeds
        super().__init__()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def create(self, **kwargs):
        kwargs = self.bind_hashed_password(kwargs)
        return super().create(json=kwargs)

    def update(self, **kwargs):
        kwargs = self.bind_hashed_password(kwargs)
        return super().update(json=kwargs)

    def update_all(self, **kwargs):
        kwargs = self.bind_hashed_password(kwargs)
        return super().update_all(json=kwargs)

    def register(self, **kwargs):
        # don't need hashed password as kwarg
        hashed_password = self.hashed_password()
        user = self.create(password=hashed_password, json=kwargs)
        login_user(user, remember=request.json.get("remember"))
        return current_user

    def login(self):
        if request.json.get("email") and request.json.get("password"):
            existing_user = self.query.filter_by(
                email=request.json.get("email")
            ).first()
            # compare against saved valid login
            if existing_user and bcrypt.check_password_hash(existing_user.password, request.json.get("password")):
                # apply logged in status for successful check
                login_user(existing_user,
                           remember=request.json.get("remember"))
                print(
                    f"ASTRO: {self.__class__.__name__} {existing_user.email} logged in successfully.\n \n")
                return current_user
            else:
                email = request.json.get("email")
                print(
                    f"ASTRO: {self.__class__.__name__} {email} unable to login, check credentials.\n \n")
                return None

    def current(self):
        if not current_user == {}:
            return current_user
        else:
            return None

    def logout(self):
        if current_user:
            temp_user = self.query.filter_by(id=current_user.id).first()
            logout_user()
            print(
                f"ASTRO: {self.__class__.__name__} {temp_user.email} logged out successfully.\n \n")
            return temp_user
        else:
            return None

    def hashed_password(self, json=None):
        if request and request.json.get("password"):
            hashed_password = bcrypt.generate_password_hash(
                request.json.get("password")).decode("utf-8")
        elif json.get("json", {}).get("password"):
            hashed_password = bcrypt.generate_password_hash(
                json.get("json", {}).get("password")).decode("utf-8")
        else:
            hashed_password = bcrypt.generate_password_hash(
                "password123").decode("utf-8")
        return hashed_password

    def bind_hashed_password(self, kwargs):
        hashed_password = self.hashed_password(json=kwargs)
        if kwargs.get("json"):
            kwargs["json"]["password"] = hashed_password
        else:
            kwargs["password"] = hashed_password
        return kwargs

    def factory(self):
        faker = Faker()
        username = faker.name().replace(" ", "")
        email = faker.email()
        json = {
            "username": username,
            "password": "123",
            "email": email
        }
        return json

    def delete_user_comments(self, comments):
        if comments == None:
            return None
        for comment in comments:
            comment.delete(comment.id)
        return None


User().seed()
