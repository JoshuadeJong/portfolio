from datetime import datetime
from flask import Blueprint, render_template, request, abort
from webApp.functions import get_static_json

projects_bp = Blueprint('projects', __name__, template_folder='html')
project_bp = Blueprint('project', __name__, template_folder='html')


@projects_bp.route('/projects.html')
def landing():
    data = get_static_json('projects.json')['projects']
    data.sort(key=order_projects_by_date)

    tags = request.args.get('tags')

    if tags:
        tags = tags.split(',')
        data = [project for project in data if set(tags) <= set(project['tags'])]

    return render_template('landing_projects.html', projects=data, tags=tags)


@project_bp.route('/projects/<title>.html')
def project(title):
    projects = get_static_json('projects.json')['projects']
    project = next((project for project in projects if project['link'] == title), None)

    if project is None:  # Project doesn't exists
        abort(404)
    if project['long'] == "" or project['long'] is None:  # Project page is under construction
        abort(501)
    else:
        return render_template('project.html', project=project)


def order_projects_by_weight(projects):
    try:
        return int(projects['weight'])
    except KeyError:
        return 0


def order_projects_by_date(project):
    if project['status'] == 'Work in Progress':
        status = 0
    elif project['status'] == 'Finished':
        status = 1
    else:
        status = -1

    try:
        date = -int(datetime.strptime(project['date'], "%b %Y").strftime("%Y%m%d"))
    except KeyError:
        date = 0
    except ValueError:
        date = 0

    output = (status, date)

    return output
