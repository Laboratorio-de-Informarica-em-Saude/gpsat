"""Blueprint api for gpsat."""
from flask import Blueprint

main_blueprint = Blueprint('gpsat_api_0', __name__, url_prefix='/api/v0')

from . import views