from flask_seeder import Seeder
from modules.app.auth.models.access_group import AccessGroup
from modules.app.auth.models.access_right import AccessRight
from modules.app.base.seeders.base import BaseSeeder
from config.app import db


class AccessGroupSeeder(BaseSeeder, Seeder):
    def __init__(self):
        self.priority = 20
        self._class = AccessGroup
        super().__init__(db=db)

    def seeds(self):
        return [
            {
                "name": "system",
                "access_group_access_right": AccessRight().model_get()
            },
            {
                "name": "administrator",
                "access_group_access_right": AccessRight().model_get()
            },
            {
                "name": "user",
                "access_group_access_right": AccessRight().model_get(default=True)
            }
        ]
