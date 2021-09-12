from flask import Flask
print("hello world !!!!!")
app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello_world():
  return "hello world118"

if __name__ == '__main__':
  app.run(debug=True)
  