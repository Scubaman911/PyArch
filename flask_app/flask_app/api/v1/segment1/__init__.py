from flask import Blueprint

from . import info, users

seg1_bp = Blueprint("segment1", __name__, url_prefix="/segment1")

seg1_bp.register_blueprint(info.blueprint)
seg1_bp.register_blueprint(users.blueprint)
