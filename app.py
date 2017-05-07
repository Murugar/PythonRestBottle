from bottle import default_app, route, response, run, template
from random import randint
from json import dumps

@route('/')
def hello_world():
  return 'Hello from Bottle!'

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/rest/getarray')
def returnarray():
    rv = [{ "id": 1, "random": randint(1000,9999), "attempts":"37" }, { "id": 2, "random": randint(1000,9999), "attempts" : "40" }]
    return dict(data=rv)

application = default_app()

run(host="localhost", port=8080)

