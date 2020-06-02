from flask import Flask
from webApp.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from webApp.pages.errors.handlers import errors_bp
app.register_blueprint(errors_bp)
from webApp.pages.home.routes import home_bp  # Add Homepage
app.register_blueprint(home_bp)
from webApp.pages.timeline.routes import timeline_bp # Add About page
app.register_blueprint(timeline_bp)
from webApp.pages.projects.routes import projects_bp # Add Projects page
app.register_blueprint(projects_bp)
from webApp.pages.projects.routes import project_bp # Add Project page
app.register_blueprint(project_bp)
from webApp.pages.about.routes import about_bp # Add About page
app.register_blueprint(about_bp)


if __name__ == '__main__':
    print("running py app")
    app.run(host="127.0.0.1", port=5000, debug=True)
