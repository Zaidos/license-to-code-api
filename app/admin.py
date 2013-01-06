from app import app, db
from app.auth import requires_auth
from app.models import License
from flask.ext.admin import Admin
from flask.ext.admin.base import AdminIndexView, expose
from flask.ext.admin.contrib.sqlamodel import ModelView

class AdminView(AdminIndexView):
  @expose('/')
  @requires_auth
  def index(self):
    return super(AdminView, self).index()

class LicenseView(ModelView):
  column_exclude_list = ('description')

  @expose('/')
  @requires_auth
  def index_view(self):
    return super(LicenseView, self).index_view()

  @expose('/new/', methods=('GET', 'POST'))
  @requires_auth
  def create_view(self):
    return super(LicenseView, self).create_view()

  @expose('/edit/', methods=('GET', 'POST'))
  @requires_auth
  def edit_view(self):
    return super(LicenseView, self).edit_view()

  @expose('/delete/', methods=('POST',))
  @requires_auth
  def delete_view(self):
    return super(LicenseView, self).delete_view()

  @expose('/action/', methods=('POST',))
  def action_view(self):
    return super(LicenseView, self).action_view()


  def __init__(self, session, **kwargs):
    super(LicenseView, self).__init__(License, session, **kwargs)

admin = Admin(name='LTC API Admin',index_view=AdminView())
admin.init_app(app)
admin.add_view(LicenseView(db.session))
