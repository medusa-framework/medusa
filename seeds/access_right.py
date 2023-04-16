from flask_seeder import Seeder
from modules.app.auth.models.access_right import AccessRight
from modules.app.base.seeders.base import BaseSeeder
from config.app import db


class AccessRightSeeder(BaseSeeder, Seeder):
    def __init__(self):
        self.priority = 10
        self._class = AccessRight
        super().__init__(db=db)

    def seeds(self):
        return [
            {
                "name": "create_user",
                "model": "User"
            },
            {
                "name": "get_user",
                "model": "User"
            },
            {
                "name": "update_user",
                "model": "User"
            },
            {
                "name": "delete_user",
                "model": "User"
            },
            {
                "name": "create_language",
                "model": "Language"
            },
            {
                "name": "get_language",
                "model": "Language"
            },
            {
                "name": "update_language",
                "model": "Language"
            },
            {
                "name": "delete_language",
                "model": "Language"
            }
        ]
