import os

from flask import Flask
from flask.ext.restful import Resource, Api

from models import *

app = Flask(__name__)
api = Api(app) 

api.add_resource(License, '/<string:license_id>')

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
