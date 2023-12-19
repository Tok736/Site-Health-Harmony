from flask import render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

from app import app
from db import db
from models import User, Doctor, Service, ServiceGroup
from forms import SignInForm, SignUpForm

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    form = SignInForm()
    
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if user is not None and check_password_hash(user.password_hash, password):
            flash("Авторизация успешна")
            login_user(user)
        else:
            flash("Неправильный логин или пароль")

    return render_template("sign_in.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    form = SignUpForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        password_repeat = form.password_repeat.data
        if len(User.query.filter_by(email=email).all()) > 0:
            flash("Пользователь с таким email уже существует")
        elif password == password_repeat:
            u = User(email=email, password_hash=generate_password_hash(password))
            db.session.add(u)
            db.session.commit()
            flash("Регистрация прошла успешно!")
        else:
            flash("Пароли должны быть одинаковыми!")

    return render_template("sign_up.html", form=form)

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
    services = Service.query.all()
    service_groups = ServiceGroup.query.all()
    return render_template("service.html", services=services, service_groups=service_groups)
