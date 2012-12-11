from flask import Flask
from flask.ext.restful import Resource, Api

from models import *

app = Flask(__name__)
api = Api(app) 

api.add_resource(License, '/<string:license_id>')

if __name__ == '__main__':
  app.run(debug=True)
