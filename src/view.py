from flask import render_template

from src.app import app
from src.models import Doctor

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

@app.route("/doctors/<int:doctor_id>")
def doctor_page(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    return render_template("doctor_page.html", doctor=doctor)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/service")
def service():
    return render_template("service.html")
