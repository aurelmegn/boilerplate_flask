# Import flask and template operators
from flask import Flask, render_template

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')
from src.controllers import *


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.jinja'), 404


@app.errorhandler(500)
def not_found(error):
    return render_template('errors/500.jinja'), 500
