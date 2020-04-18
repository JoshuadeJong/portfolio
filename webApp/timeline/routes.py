from flask import Blueprint, render_template

timeline_bp = Blueprint('timeline', __name__, template_folder='html')

@timeline_bp.route('/timeline')
def landing():
    return render_template('landing_timeline.html')