from faker import Faker
from flask import request
from flask_login import login_user, current_user, logout_user
from medusa import db, bcrypt, login_manager
from medusa.modules.app.base.models.base import Base
from medusa.modules.app.user.controllers.user import UserController
from flask_login import UserMixin
from medusa.modules.app.user.models.access_group import AccessGroup
from medusa.modules.app.user.routes.user import UserRoute
from medusa.modules.app.user.seeders.user import users as seeds


user_access_groups = db.Table(
    "user_access_groups",
    db.Column("access_group_id", db.Integer, db.ForeignKey(
        "access_group.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey(
        "user.id"), primary_key=True)
)


class User(Base, UserRoute, db.Model, UserMixin):

    username = db.Column(db.String(128))
    password = db.Column(db.String())
    email = db.Column(db.String(120))
    comments = db.relationship("Comment", backref="user", lazy=True)
    notifications = db.relationship("Notification", backref="user", lazy=True)
    user_access_groups = db.relationship(
        "AccessGroup",
        secondary=user_access_groups,
        lazy="subquery",
        backref=db.backref("user", lazy=True)
    )

    def __init__(self) -> None:
        self._controller = UserController(self)
        self._seeds = seeds
        super().__init__()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def create(self, **kwargs):
        kwargs["password"] = self.hashed_password(**kwargs)
        return self.post(**kwargs)

    def update(self, **kwargs):
        kwargs["password"] = self.hashed_password(**kwargs)
        return self.post(**kwargs)

    def post(self, **kwargs):
        access_groups = kwargs.get("user_access_groups")
        if access_groups:
            access_group_records = []
            for access_group in access_groups:
                access_group_record = AccessGroup().query.filter_by(
                    id=access_group).first()
                if access_group_record:
                    access_group_records.append(access_group_record)
            kwargs["user_access_groups"] = access_group_records
        kwargs = self.bind_hashed_password(kwargs)
        if kwargs.get("request_type") == "PATCH":
            return super().update(**kwargs)
        elif kwargs.get("request_type") == "POST":
            return super().create(**kwargs)

    def update_all(self, **kwargs):
        kwargs = self.bind_hashed_password(kwargs)
        return super().update_all(json=kwargs)

    def register(self, **kwargs):
        # don't need hashed password as kwarg
        hashed_password = self.hashed_password(**kwargs)
        user = self.create(password=hashed_password, json=kwargs)
        login_user(user, remember=request.json.get("remember"))
        return current_user

    def login(self, **kwargs):
        if kwargs.get("email") and kwargs.get("password"):
            existing_user = self.query.filter_by(
                email=kwargs.get("email")
            ).first()
            # compare against saved valid login
            # if existing_user and bcrypt.check_password_hash(existing_user.password, kwargs.get("password")):
            # apply logged in status for successful check
            login_user(existing_user,
                       remember=kwargs.get("remember"))
            return current_user
            # else:
            #     return None

    def current(self):
        if not current_user == {}:
            return current_user
        else:
            return None

    def logout(self):
        if current_user:
            temp_user = self.query.filter_by(id=current_user.id).first()
            logout_user()
            return temp_user
        else:
            return None

    def hashed_password(self, **kwargs):
        if kwargs.get("password"):
            hashed_password = bcrypt.generate_password_hash(
                kwargs.get("password")).decode("utf-8")
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


User()
