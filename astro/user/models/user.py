from astro import db, login_manager, bcrypt
from astro.base.models.base import Base
from flask_login import login_user, logout_user, current_user, UserMixin
from flask import request


class User(db.Model, Base, UserMixin):
    username = db.Column(db.String(128))
    password = db.Column(db.String())
    email = db.Column(db.String(120))

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def create(self, json=None, **kwargs):
        if request.json.get("password"):
            hashed_password = bcrypt.generate_password_hash(
                request.json.get("password")).decode("utf-8")
        return super().create(password=hashed_password)

    def register(self, json=None, **kwargs):
        user = self.create()
        login_user(user, remember=request.json.get("remember"))
        return current_user

    def login(self):
        if request.json.get("email") and request.json.get("password"):
            existing_user = self.query.filter_by(
                email=request.json.get("email")
            ).filter_by(deleted=False).first()
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
