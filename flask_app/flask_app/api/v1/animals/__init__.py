from flask import Blueprint

from . import info, users

seg1_bp = Blueprint("animals", __name__, url_prefix="/animals")

seg1_bp.register_blueprint(info.blueprint)
seg1_bp.register_blueprint(users.blueprint)
