from flask import Blueprint, render_template
from webApp.functions import get_static_json

about_bp = Blueprint('about', __name__, template_folder='html')


@about_bp.route('/about')
def landing():
    data_about = get_static_json('about.json')
    data_project = get_static_json('projects.json')['projects']
    data_project.sort(key=order_projects_by_weight)
    data_project = data_project[0:3]

    return render_template('landing_about.html', projects=data_project, about=data_about)


def order_projects_by_weight(projects):
    try:
        return int(projects['weight'])
    except KeyError:
        return 0