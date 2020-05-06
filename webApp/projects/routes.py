from flask import Blueprint, render_template, request
import io, json, os
from datetime import datetime

projects_bp = Blueprint('projects', __name__, template_folder='html')
project_bp = Blueprint('project', __name__, template_folder='html')



@projects_bp.route('/projects')
def landing():
    data = get_static_json('projects.json')['projects']
    data.sort(key=order_projects_by_date, reverse=True)

    tag = request.args.get('tags')
    if tag:
        data = [project for project in data if tag.lower() in [project_tag.lower() for project_tag in project['tags']]]

    return render_template('landing_projects.html', projects= data, tag= tag)

@project_bp.route('/projects/<title>')
def project():
    pass


def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(site_root, path)


def get_static_json(path):
    return json.load(open(get_static_file(path)))


def order_projects_by_weight(projects):
    try:
        return int(projects['weight'])
    except KeyError:
        return 0

def order_projects_by_date(projects):
    try:
        return int(datetime.strptime(projects['date'], "%b %Y").strftime("%Y%m%d"))
    except KeyError:
        return 0
    except ValueError:
        return 0
