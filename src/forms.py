from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class SignUpForm(FlaskForm):
    email = EmailField("Имя", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(8, 24)])
    password_repeat = PasswordField("Повторите пароль", validators=[DataRequired(), Length(8, 24)])
