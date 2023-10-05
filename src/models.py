from db import db

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    second_name = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"<Doctor {self.first_name} {self.second_name}>"
