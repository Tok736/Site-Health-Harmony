from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from src.app import app
from src.db import db
from src.models import User, Doctor, Service, ServiceGroup

admin = Admin(app, __name__, template_mode="bootstrap3")

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Doctor, db.session))
admin.add_view(ModelView(Service, db.session))
admin.add_view(ModelView(ServiceGroup, db.session))

