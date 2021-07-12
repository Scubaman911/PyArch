"""Public section, including homepage and signup."""
from flask import Blueprint, current_app, request
from spectree import Response

from flask_app.extensions import api_spec
from flask_app.data.pydantic import QInfoModel, RInfoModel


blueprint = Blueprint("info", __name__, url_prefix="/info")


@blueprint.route("/", methods=["POST"])
@api_spec.validate(json=QInfoModel, resp=Response(HTTP_200=RInfoModel), tags=["v1"])
def info():
    """Get info by animal name...it only knows kangaroo"""
    current_app.logger.info("Hello from the home page!")
    animal = request.json.get("animal")

    if animal == "kangaroo":
        resp = RInfoModel(id=1, name="kangaroo", fun_fact="Kangaroos Are the Largest Marsupials on Earth")
    else:
        resp = RInfoModel(id=0, name=animal, fun_fact="Unknown animal")

    return resp.dict()