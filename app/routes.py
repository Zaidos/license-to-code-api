from app import app
from app.models import License
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

  if v is not None:
    licenses = License.query.filter_by(abbv=slug).filter_by(version = v)
  else:
    licenses = License.query.filter_by(abbv=slug)

  license = licenses.first()

  if license is None:
    return not_found("sorry, but this doesn't event exist")

  return flask.jsonify(license.to_json())

@app.errorhandler(404)
def not_found(error):
  return "%s" % error, 404
