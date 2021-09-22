from flask import Blueprint, render_template
from algorithm.images import image_data


starter_bp = Blueprint('starter', __name__,
                       url_prefix='/starter',
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='static/assets')






