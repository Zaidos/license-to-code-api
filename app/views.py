from app import admin, db
from app.models import License
from flask.ext.admin.contrib.sqlamodel import ModelView

admin.add_view(ModelView(License, db.session))
