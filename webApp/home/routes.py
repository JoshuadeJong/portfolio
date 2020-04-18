from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__, template_folder='html')

@home_bp.route('/')
@home_bp.route('/home')
def landing():
    return render_template('landing_home.html')