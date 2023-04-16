from flask_seeder import Seeder
from modules.app.auth.models.access_group import AccessGroup
from modules.app.base.seeders.base import BaseSeeder
from modules.app.auth.models.user import User
from config.app import db


class UserSeeder(BaseSeeder, Seeder):
    def __init__(self):
        self.priority = 100
        self._class = User
        super().__init__(db=db)

    def seeds(self):
        return [
            {
                "username": "system",
                "email": "system@medusa.com",
                "display_name": "System",
                "password": "medusa",
                "user_access_group": AccessGroup().model_get()
            },
            {
                "username": "administrator",
                "email": "administrator@medusa.com",
                "display_name": "Administrator",
                "password": "medusa",
                "user_access_group": AccessGroup().model_get()
            }
        ]
