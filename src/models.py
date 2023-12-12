from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.sql import func 
from sqlalchemy.orm import Relationship

from db import db

class User(db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    password_hash = Column(String(100))

    first_name = Column(String(100))
    second_name = Column(String(100))
    patronymic = Column(String(100))
    age = Column(Integer)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())

    def __repr__(self):
        return f"<User {self.first_name} {self.second_name}>"

class Doctor(db.Model):
    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"), nullable=False)
    user = Relationship("User")
    experience = Column(String(50))

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())

    def __repr__(self):
        return f"<Doctor {self.user.first_name} {self.user.second_name}>"

class Service(db.Model):
    __tablename__ = "service"

    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text())
    service_group_id = Column(ForeignKey("service_group.id"))
    service_group = Relationship("ServiceGroup")

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())

    def __repr__(self):
        return f"<Service {self.name}>"

class ServiceGroup(db.Model):
    __tablename__ = "service_group"

    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text())

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())

    def __repr__(self):
        return f"<ServiceGroup {self.name}>"
