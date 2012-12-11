from flask import request
from flask.ext.restful import Resource

licenses = {}

class License(Resource):
  def get(self, license_id):
    return { license_id : licenses[license_id] }

  def put(self, license_id):
    licenses[license_id] = request.form['data']
    return { license_id : licenses[license_id] }
