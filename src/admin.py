from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import app
from db import db
from models import User, Doctor, Service, ServiceGroup

admin = Admin(app, __name__, template_mode="bootstrap3")

# class UserModelView(ModelView):


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Doctor, db.session))
admin.add_view(ModelView(Service, db.session))
admin.add_view(ModelView(ServiceGroup, db.session))
