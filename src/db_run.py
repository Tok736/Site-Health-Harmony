from db import db
from app import app
from models import Doctor

with app.app_context():
    db.drop_all()
    db.create_all()

with app.app_context():
    doctor = Doctor(first_name="Alexandr", second_name="Ivanov", age=47)
    db.session.add(d)
    db.session.commit()

# with app.app_context():
#     doctors = Doctor.query.all()
#     print(doctors)

