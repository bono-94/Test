from flask import Flask
import myfile

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/sayhello/<name>")
def secondmethod(name):
    return "<p>Hello, </p>"+name


@app.route("/saythird/<variable>")
def thirdmethod(variable):
    return myfile.thisismymethod(variable)
