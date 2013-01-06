#!/usr/bin/env python

import os

from flask import Flask
from flask_heroku import Heroku
from flask.ext.admin import Admin
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

heroku = Heroku(app)
db = SQLAlchemy(app)
admin = Admin(app, name="LTC API")

# Import routes
from app import models
from app import routes
from app import views
