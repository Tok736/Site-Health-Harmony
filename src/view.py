from flask import render_template

from app import app
from models import Doctor

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/doctors")
def doctors():
    doctors = Doctor.query.all()
    return render_template("doctors.html", doctors=doctors)
