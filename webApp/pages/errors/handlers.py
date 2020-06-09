from flask import Blueprint, render_template

errors_bp = Blueprint('errors', __name__, template_folder='html')


@errors_bp.app_errorhandler(404)
def error_404(error):
    return render_template('404.html')


@errors_bp.app_errorhandler(403)
def error_403(error):
    return render_template('403.html')


@errors_bp.app_errorhandler(500)
def error_500(error):
    return render_template('500.html')


@errors_bp.app_errorhandler(501)
def error_501(error):
    return render_template('501.html')
