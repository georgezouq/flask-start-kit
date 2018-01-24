from flask_restful import Resource
from .Todo import TODOS


class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

