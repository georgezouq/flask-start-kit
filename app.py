from flask import Flask
from flask_cors import CORS
from resources import todo, user, auth
from extensions import db, jwt
from common.config import SECRET_KEY

def create_app():
    app = Flask(__name__)
    CORS(app)

    configure_extensions(app)
    register_blueprints(app)
    return app


def configure_extensions(app):
    db.init_app(app)
    app.config.setdefault('JWT_SECRET_KEY', SECRET_KEY)
    jwt.init_app(app)


def register_blueprints(app):
    app.register_blueprint(user.blueprint, url_prefix='/users')
    app.register_blueprint(todo.blueprint, url_prefix='/todos')
    # app.register_blueprint(user.blueprint, url_prefix='/user')
    app.register_blueprint(auth.login.blueprint, url_prefix='/auth')
