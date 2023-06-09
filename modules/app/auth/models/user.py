from config.system import db, bcrypt, login_manager, mail
from modules.app.auth.emails.register import RegisterEmail
from modules.app.auth.factories.user import UserFactory
from modules.app.base.models.base import BaseModel
from modules.app.auth.controllers.user import UserController
from modules.app.auth.routes.user import UserRoute
from flask_login import login_user, current_user, logout_user, UserMixin, login_required

"""
Defines a pivot table relationship between Users and Access Groups.
"""
user_access_group = db.Table(
    "user_access_group",
    db.Column("access_group_id", db.Integer, db.ForeignKey(
        "access_group.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey(
        "user.id"), primary_key=True)
)


class User(BaseModel, UserRoute, UserController, UserFactory, UserMixin, db.Model):
    """
    Represents a User in the application.

    Attributes:
        username (str): The username of the User.
        email (str): The email address of the User.
        password (str): The hashed password of the User.
        first_name (str): The first name of the User.
        last_name (str): The last name of the User.
        display_name (str): The display name of the User.
        phone (str): The phone number of the User.
        comments (list[Comment]): The Comments made by the User.
        user_access_group (list[AccessGroup]): The Access Groups associated with the User.
    """
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    comments = db.relationship('Comment', backref='user', lazy=True)
    user_access_group = db.relationship(
        "AccessGroup",
        secondary=user_access_group,
        lazy="subquery",
        backref=db.backref("user", lazy=True)
    )


    def __init__(self, **kwargs) -> None:
        """
        Initializes a new User instance that takes in keyword arguments.
        Should return super init call.

        Args:
            username (optional): The username of the User.
            email (optional): The email address of the User.
            password (optional): The hashed password of the User.
            first_name (optional): The first name of the User.
            last_name (optional): The last name of the User.
            display_name (optional): The display name of the User.
            phone (optional): The phone number of the User.
            comments (optional): The Comments made by the User.
            user_access_group (optional): The Access Groups associated with the User.
        """
        super().__init__(**kwargs)

    @login_manager.user_loader
    def load_user(user_id) -> object:
        """
        Loads a User from the database based on the User id.

        Args:
            user_id: The id of the User.

        Returns:
            The User object corresponding to the User id.
        """
        return User.query.get(int(user_id))

    def model_create(self, **kwargs) -> object:
        """
        Creates a new User in the database.

        Args:
            username (optional): The username of the User.
            email (optional): The email address of the User.
            password (optional): The hashed password of the User.
            first_name (optional): The first name of the User.
            last_name (optional): The last name of the User.
            display_name (optional): The display name of the User.
            phone (optional): The phone number of the User.
            comments (optional): The Comments made by the User.
            user_access_group (optional): The Access Groups associated with the User.

        Returns:
            The created User object.
        """
        kwargs["password"] = self.hashed_password(kwargs.get("password"))
        RegisterEmail([kwargs.get("email")], **kwargs).send_email()
        return super().model_create(**kwargs)

    def hashed_password(self, password=None) -> str:
        """
        Hashes the provided password using bcrypt.

        Args:
            password: The password to be hashed.

        Returns:
            (str) The hashed password.
        """
        hashed_password = bcrypt.generate_password_hash(
            password).decode("utf-8")
        return hashed_password

    def model_login(self, **request_json):
        if request_json.get("email") and request_json.get("password"):
            record = self.query.filter_by(
                email=request_json.get("email")).first()
            if record and bcrypt.check_password_hash(record.password, request_json.get("password")):
                login_user(record, remember=request_json.get("remember"))
                return current_user

    def model_logout(self):
        if current_user.is_authenticated:
            user = self.query.filter_by(id=current_user.id).first()
            logout_user()
            return user

    def model_current(self):
        if current_user.is_authenticated:
            return current_user
        else:
            return None

    def model_comments(self, **request_args):
        users = self.model_get(**request_args)
        comments = [comment for user in users for comment in user.comments]
        return comments
    


