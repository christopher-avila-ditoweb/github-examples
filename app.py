from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/one")
def page_one():
    return render_template("one.html")

@app.route("/two")
def page_two():
    return "<p>page 2</p>"

@app.route("/three")
def page_three():
    return "<p>page 3</p>"
