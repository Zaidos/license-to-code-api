from app import admin
from flask import Flask
from flask.ext.admin import Admin, BaseView, expose

class LicensesView(BaseView):
  @expose('/')
  def index(self):
    return self.render('index.html')

admin.add_view(LicensesView(name="Licenses"))
