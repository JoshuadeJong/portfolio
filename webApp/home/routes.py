from flask import Blueprint, render_template
from webApp.functions import get_static_json

home_bp = Blueprint('home', __name__, template_folder='html')

@home_bp.route('/')
@home_bp.route('/home')
def landing():
    data = get_static_json('about.json')
    return render_template('landing_home.html', data=data)