from flask import Flask
from flask_cors import CORS
from resources import todo, user, auth
from extensions import db, jwt


def create_app():
    app = Flask(__name__)
    CORS(app)

    register_blueprints(app)
    return app


def configure_extensions(app):
    db.init_app(app)
    jwt.init_app(app)


def register_blueprints(app):
    app.register_blueprint(user.blueprint, url_prefix='/users')
    app.register_blueprint(todo.blueprint, url_prefix='/todos')
    # app.register_blueprint(user.blueprint, url_prefix='/user')
    # app.register_blueprint(auth.blueprint, url_prefix='/auth')
