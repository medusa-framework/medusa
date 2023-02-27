from astro.modules.app.sandbox.models.sandbox import Sandbox
from flask import request
# from faker import Faker
# from astro.app.user.models.user import User


class SandboxController():

    def sandbox(self):
        return Sandbox().sandbox()
