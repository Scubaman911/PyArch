from flask import Blueprint

from . import info

animals_bp = Blueprint("animals", __name__, url_prefix="/animals")

animals_bp.register_blueprint(info.blueprint)
