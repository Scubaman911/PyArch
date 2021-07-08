"""Public section, including homepage and signup."""
from flask import Blueprint, current_app

blueprint = Blueprint("home", __name__, url_prefix="/home", static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    current_app.logger.info("Hello from the home page!")
    return "Home page!"
