from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "<h1><a href=\"http://dimini.tk\">Dimini Inc</a></h1>"

@app.route("/memes")
def memes():
    return "<h1><a href=\"http://dimini.tk\">Dimini Inc love memes</a></h1>"

app.run()
