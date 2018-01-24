from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
from resources.todo import todo_blueprint

from resources.todo.Todo import Todos

app = Flask(__name__)
CORS(app)
api = Api(app)

app.register_blueprint(todo_blueprint, url_prefix='/todo')
# api.add_resource(Todos, '/todo', '/todo/<str:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)