from flask import Blueprint, render_template
import json, os
from webApp.functions import get_static_json

timeline_bp = Blueprint('timeline', __name__, template_folder='html')

@timeline_bp.route('/timeline.html')
def landing():
    data = get_static_json('timeline.json')['years']
    return render_template('landing_timeline.html', years=data)