from db import db
from app import app
from models import Doctor, User

with app.app_context():
    db.drop_all()
    db.create_all()

with app.app_context():
    user = User(email="abc@mail.ru", first_name="Alexandr", second_name="Ivanov", age=47)
    db.session.add(user)
    db.session.commit()

    doctor = Doctor(user=user, experience="5 months")
    db.session.add(doctor)
    db.session.commit()

with app.app_context():
    doctors = Doctor.query.all()
    print(doctors)

