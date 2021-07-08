from flask import Blueprint

from . import segment1

v1_bp = Blueprint("v1", __name__, url_prefix="/v1")

v1_bp.register_blueprint(segment1.seg1_bp)
