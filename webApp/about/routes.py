from flask import Blueprint, render_template

about_bp = Blueprint('about', __name__, template_folder='html')


@about_bp.route('/about')
def landing():
    return render_template('landing_about.html')