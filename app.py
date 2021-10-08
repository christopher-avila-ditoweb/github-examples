from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/world")
def world():
    return render_template("world.html")