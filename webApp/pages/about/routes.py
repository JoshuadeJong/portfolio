from flask import Blueprint, render_template
from webApp.functions import get_static_json
import json

about_bp = Blueprint('about', __name__, template_folder='html')


@about_bp.route('/about.html')
def landing():
    # General about page info
    data_about = get_static_json('about.json')

    # Query for Projects
    if "projects" in data_about:
        data_project = get_static_json('projects.json')['projects']
        project_list = data_about['projects']

        for i in range(len(data_project) - 1, -1, -1):
            if data_project[i]['name'] not in project_list:
                data_project.pop(i)

    else:
        data_project = None

    return render_template('landing_about.html', projects=data_project, about=data_about)


def order_projects_by_weight(projects):
    try:
        return int(projects['weight'])
    except KeyError:
        return 0