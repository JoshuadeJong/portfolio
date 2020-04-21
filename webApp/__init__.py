from flask import Flask
from webApp.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from webApp.errors.handlers import errors_bp
    app.register_blueprint(errors_bp)
    from webApp.home.routes import home_bp  # Add Homepage
    app.register_blueprint(home_bp)
    from webApp.timeline.routes import timeline_bp # Add About page
    app.register_blueprint(timeline_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    print("running py app")
    app.run(host="127.0.0.1", port=5000, debug=True)
