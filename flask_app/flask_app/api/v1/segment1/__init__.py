from flask import Blueprint

from . import home, users

seg1_bp = Blueprint("segment1", __name__, url_prefix="/segment1")

seg1_bp.register_blueprint(home.blueprint)
seg1_bp.register_blueprint(users.blueprint)
