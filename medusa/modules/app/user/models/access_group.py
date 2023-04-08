from faker import Faker
from medusa.modules.app.base.controllers.base import BaseController
from medusa.modules.app.base.models.base import Base
from medusa import db
from medusa.modules.app.user.models.access_right import AccessRight
from medusa.modules.app.user.seeders.access_group import access_groups as seeds


access_group_rights = db.Table(
    "access_group_rights",
    db.Column("access_right_id", db.Integer, db.ForeignKey(
        "access_right.id"), primary_key=True),
    db.Column("access_group_id", db.Integer, db.ForeignKey(
        "access_group.id"), primary_key=True)
)


class AccessGroup(Base, db.Model):
    """
    A model class for AccessGroup and its methods.

    Attributes:
        name (db.Column): A string column to store the name of the access group.
        access_group_rights (db.relationship): A many-to-many relationship to AccessRight model.
    """

    name = db.Column(db.String(50))
    access_group_rights = db.relationship(
        "AccessRight",
        secondary=access_group_rights,
        lazy="subquery",
        backref=db.backref("accessgroup", lazy=True)
    )

    def __init__(self) -> None:
        """
        Initializes a new instance of AccessGroup and its controller and seeds attributes.
        """
        self._controller = BaseController(self)
        self._seeds = seeds
        super().__init__()

    def create(self, **kwargs):
        """
        Create a new AccessGroup instance and add it to the database.

        Args:
            **kwargs: Arbitrary keyword arguments. It can include name and access_group_rights.

        Returns:
            AccessGroup: A new instance of AccessGroup.
        """
        return self.post(**kwargs)

    def update(self, **kwargs):
        """
        Update an existing AccessGroup instance and update its values in the database.

        Args:
            **kwargs: Arbitrary keyword arguments. It can include name and access_group_rights.

        Returns:
            AccessGroup: The updated instance of AccessGroup.
        """
        return self.post(**kwargs)

    def post(self, **kwargs):
        """
        Handle the POST and PATCH requests of the AccessGroup model.

        Args:
            **kwargs: Arbitrary keyword arguments. It can include name, access_group_rights, and request_type.

        Returns:
            AccessGroup: The created or updated instance of AccessGroup.
        """
        print(kwargs)
        access_rights = kwargs.get("access_group_rights")
        if access_rights:
            access_right_records = []
            for access_right in access_rights:
                access_right_record = AccessRight().query.filter_by(
                    id=access_right).first()
                if access_right_record:
                    access_right_records.append(access_right_record)
            kwargs["access_group_rights"] = access_right_records
        if kwargs.get("request_type") == "PATCH":
            return super().update(**kwargs)
        elif kwargs.get("request_type") == "POST":
            return super().create(**kwargs)

    def factory(self):
        """
        Create a new AccessGroup instance with a randomly generated name.

        Returns:
            dict: A new instance of AccessGroup with a random name.
        """
        faker = Faker()
        name = faker.word()
        json = {"name": name}
        return json


AccessGroup()
