from flask_seeder import Seeder
from modules.base.seeders.base import BaseSeeder
from modules.auth.models.user import User
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
                "password": "medusa"
            },
            {
                "username": "administrator",
                "email": "administrator@medusa.com",
                "display_name": "Administrator",
                "password": "medusa"
            }
        ]
