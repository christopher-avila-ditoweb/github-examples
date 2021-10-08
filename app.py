from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def page_one():
    return "<p>page 1</p>"

@app.route("/")
def page_two():
    return "<p>page 2</p>"