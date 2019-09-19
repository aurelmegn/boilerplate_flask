from src import app
from flask import render_template, request

@app.route("/")
def index():
    return render_template("default/index.jinja")
