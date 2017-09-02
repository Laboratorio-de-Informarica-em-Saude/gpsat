"""Blueprint api for gpsat."""
from flask import Blueprint

api = Blueprint('api', __name__)

from . import form, errors, auth


def create_app(config_name):
    """Create app for api gpsat."""
    from .api import api as api_1_blueprint
    app.register_blueprint(api_1_blueprint, url_prefix='/api/v1')
