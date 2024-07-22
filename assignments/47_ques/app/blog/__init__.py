from flask import Blueprint

# Create a Blueprint instance
blog_bp = Blueprint('blog', __name__, template_folder='templates', static_folder='static')

from . import routes  # Import routes to register them with the blueprint
