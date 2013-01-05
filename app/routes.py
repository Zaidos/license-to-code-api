from app import app
from app.models import License
from sqlalchemy import func
import flask
import json

@app.route('/favicon.ico')
def fav_icon():
  return ''

@app.route('/')
def home():
  limit = flask.request.args.get('limit')
  offset = flask.request.args.get('offset')

  results = License \
    .query \
    .order_by(License.name) \
    .limit(limit) \
    .all()

  return flask.jsonify(licenses = [license.to_json() for license in results])

@app.route('/<string:slug>')
def get(slug):
  v = flask.request.args.get('v')

  licenses = License.query.filter(func.lower(License.abbv) == func.lower(slug))

  if v is not None:
    licenses = licenses.filter_by(version = v.lower())

  license = licenses.first()

  if license is None:
    return not_found("sorry, but this doesn't event exist")

  return flask.jsonify(license.to_json())

@app.errorhandler(404)
def not_found(error):
  return "%s" % error, 404
