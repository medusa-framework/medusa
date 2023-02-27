from astro.sandbox.models.sandbox import Sandbox
from flask import request
from faker import Faker
from astro.user.models.user import User


class SandboxController():

    def sandbox(self):
        return Sandbox().sandbox()
