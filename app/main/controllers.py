from flask import Flask
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)
