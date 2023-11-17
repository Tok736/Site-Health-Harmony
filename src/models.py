from db import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    first_name = db.Column(db.String(100), nullable=False)
    second_name = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"<User {self.first_name} {self.second_name}>"

class Doctor(db.Model):
    __tablename__ = "doctor"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey("user.id"), nullable=False)
    user = db.Relationship("User")
    experience = db.Column(db.String(50))

    def __repr__(self):
        return f"<Doctor {self.user.first_name} {self.user.second_name}>"

class Service(db.Model):
    __tablename__ = "service"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text())
    service_group_id = db.Column(db.ForeignKey("service_group.id"))
    service_group = db.Relationship("ServiceGroup")

    def __repr__(self):
        return f"<Service {self.name}>"

class ServiceGroup(db.Model):
    __tablename__ = "service_group"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text())

    def __repr__(self):
        return f"<ServiceGroup {self.name}>"
