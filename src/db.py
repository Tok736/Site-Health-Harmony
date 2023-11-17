from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.app import app

db = SQLAlchemy(app)
migrate = Migrate(app, db, command="db")
