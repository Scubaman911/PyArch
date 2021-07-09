from flask import Blueprint

from . import animals

v1_bp = Blueprint("v1", __name__, url_prefix="/v1")

v1_bp.register_blueprint(animals.seg1_bp)
