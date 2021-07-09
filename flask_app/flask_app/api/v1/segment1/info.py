"""Public section, including homepage and signup."""
from flask import Blueprint, current_app
from flask_pydantic import validate

blueprint = Blueprint("info", __name__, url_prefix="/info", static_folder="../static")


@blueprint.route("/", methods=["GET"])
@validate()
def get():
    """Home page."""
    current_app.logger.info("Hello from the home page!")
    return "Home page!"
