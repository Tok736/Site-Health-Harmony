from flask import Flask
from flask_admin import Admin

app = Flask(__name__, template_folder="../templates", static_folder="../static")

app.config.from_pyfile("config.py")

