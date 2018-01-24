from flask import Blueprint
from flask_restful import Api
from .Todo import Todos
from .TodoList import TodoList

todo_blueprint = Blueprint('todo', __name__)
api = Api(todo_blueprint)

api.add_resource(TodoList, '/todos')
api.add_resource(Todos, '/<string:todo_id>')