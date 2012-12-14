#!/usr/bin/env python

import os

from flask import Flask
from flask_heroku import Heroku
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

heroku = Heroku(app)
db = SQLAlchemy(app)

# Import routes
from app import models
from app import routes
