from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class SignUpForm(FlaskForm):
    email = EmailField("Имя", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    password_repeat = PasswordField("Повторите пароль", validators=[DataRequired()])

class SignInForm(FlaskForm):
    email = EmailField("Имя", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])

