from flask import Blueprint
from astro.sandbox.controllers.sandbox import SandboxController
from astro.sandbox.models.sandbox import Sandbox
from astro.utils.functions.utils import to_json

sandbox = Blueprint("sandbox", __name__)


@sandbox.route("/sandbox", methods=["POST"])
def route():
    return to_json(SandboxController().sandbox())
