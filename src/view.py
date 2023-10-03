from flask import render_template

from app import app
from models import Doctor

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/other")
def other():
    return render_template("other.html")

@app.route("/doctors")
def doctors():
    doctors = Doctor.query.all()
    return render_template("doctors.html", doctors=doctors)
