from flask_restful import Resource, abort, reqparse

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="TODO {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('task')

class Todos(Resource):

    def get(self, todo_id):
        print('todo_id:', todo_id)
        if_todo_doesnt_exist(todo_id)
        return {todo_id: TODOS[todo_id]}

    def delete(self, todo_id):
        if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        TODOS[todo_id] = args['task']
        task = {todo_id: TODOS[todo_id]}
        TODOS[todo_id] = task
        return task, 201


