from flask import Flask

print("hello world !!!!!")
app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello_world():
  return "hello world118"

@app.route("/test/<s_query>")
def search(s_query):
  return s_query


@app.route("/integer/<int:value>")
def int_type(value):
  print(value + 1)
  return "correct"

@app.route("/float/<float:value>")
def float_type(value):
  print(value + 1.45, flush=True)
  return "correct"

@app.route("/path/<path:value>")
def path_type(value):
  print( value, flush=True)
  return "correct"

@app.route("/name/<name>")
def index(name):
  if name.lower() == "michael":
    return "Hello, {}".format(name), 200
  else:
    return "Not found", 404 


if __name__ == '__main__':
  app.run(debug=True)
  