# Import flask and template operators
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_webpackext import FlaskWebpackExt, WebpackBundleProject
from src.utils.format_datetime import date_format_datetime
from dynaconf import FlaskDynaconf

webpack_project = WebpackBundleProject(
    __name__, project_folder="assets", config_path="./public/entrypoint.json"
)

# Define the WSGI application object
app = Flask(__name__, static_folder="public")

FlaskDynaconf(app)

FlaskWebpackExt(app)

app.config.update(dict(WEBPACKEXT_PROJECT=webpack_project))


if app.config.get("ENV").startswith("dev"):
    from flask_debugtoolbar import DebugToolbarExtension

    # debug toolbar
    toolbar = DebugToolbarExtension(app)
    
# Sql alchemy
db = SQLAlchemy(app)

# Template engine setup
app.jinja_env.filters['datetime'] = date_format_datetime

from src.controllers import *

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.jinja'), 404


@app.errorhandler(500)
def not_found(error):
    return render_template('errors/500.jinja'), 500
