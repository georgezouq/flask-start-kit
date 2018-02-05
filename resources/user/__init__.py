from flask import Blueprint
from flask_restful import Api
from .user import UserResource, UserList

blueprint = Blueprint('api', __name__, url_prefix='/api/users')
api = Api(blueprint)

api.add_resource(UserResource, '/<int:user_id>')
api.add_resource(UserList, '/')