import logging
from flask import Blueprint, jsonify, render_template, request, session, Response
from utils.session import check_session_validity
from limiter import limiter

logger = logging.getLogger(__name__)

technical_bp = Blueprint('technical_bp', __name__, url_prefix='/technical')

@technical_bp.route('/', methods=['GET'])
@check_session_validity
@limiter.limit("60/minute")
def index():  # Rename function to match the endpoint name
    """Display technical monitoring dashboard"""
    return render_template('technical/dashboard.html')
