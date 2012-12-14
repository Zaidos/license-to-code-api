from app import db

class License(db.Model):
  __tablename__ = 'licenses'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(256))
  abbv = db.Column(db.String(25))
  version = db.Column(db.String(25))
  description = db.Column(db.Text)

  def __init__(self, name, version = "0.0", abbv = "", description = ""):
    self.name = name
    self.version = version
    self.abbv = abbv
    self.description = description

  def __repr__(self):
    return "<License %s (%r)>" % (self.name, self.version)

  def to_json(self):
    return {
      'name' : self.name,
      'version' : self.version,
      'abbv' : self.abbv,
      'description' : self.description
    }
