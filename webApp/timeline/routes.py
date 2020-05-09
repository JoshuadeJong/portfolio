from flask import Blueprint, render_template
import json, os

timeline_bp = Blueprint('timeline', __name__, template_folder='html')

@timeline_bp.route('/timeline')
def landing():
    data = get_static_json('timeline.json')['years']
    return render_template('landing_timeline.html', years=data)

def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(site_root, path)


def get_static_json(path):
    return json.load(open(get_static_file(path)))