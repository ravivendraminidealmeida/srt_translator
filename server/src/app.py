from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from db import db
from models import Translation

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return Translation.query.all()