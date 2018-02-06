from flask import Blueprint
from flask_restful import Api
from .Todo import Todos
from .TodoList import TodoList

blueprint = Blueprint('todo', __name__)
api = Api(blueprint)

api.add_resource(TodoList, '/')
api.add_resource(Todos, '/<string:todo_id>')