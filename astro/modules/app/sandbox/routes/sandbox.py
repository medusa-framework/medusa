from flask import Blueprint
from astro.modules.app.sandbox.controllers.sandbox import SandboxController
from astro.modules.app.sandbox.models.sandbox import Sandbox
from astro.modules.app.utils.functions.utils import to_json

sandbox = Blueprint("sandbox", __name__)


@sandbox.route("/sandbox", methods=["POST"])
def route():
    return to_json(SandboxController().sandbox())
