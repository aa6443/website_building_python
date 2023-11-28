from flask import Flask
#app is object of the class flask
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, Aniket"


if __name__ == "__main__":
 app.run(host='0.0.0.0',debug=True)
