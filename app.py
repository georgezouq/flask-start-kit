from flask import Flask
from flask_cors import CORS
from resources import todo, user, auth
from extensions import db, jwt
from common.config import SECRET_KEY, SQLALCHEMY_TRACK_MODIFICATIONS, db_path
import models


def create_app():
    app = Flask(__name__)
    CORS(app)

    configure_extensions(app)
    register_blueprints(app)
    return app


def configure_extensions(app):
    app.config.setdefault('JWT_SECRET_KEY', SECRET_KEY)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)
    jwt.init_app(app)

    db.create_all(app=app)


def register_blueprints(app):
    app.register_blueprint(user.blueprint, url_prefix='/users')
    app.register_blueprint(todo.blueprint, url_prefix='/todos')
    # app.register_blueprint(user.blueprint, url_prefix='/user')
    app.register_blueprint(auth.login.blueprint, url_prefix='/auth')
