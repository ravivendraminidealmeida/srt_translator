import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models import Translation
from db import db
from schemas import marsh

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_CONNECTION
app.config["UPLOAD_FOLDER"] = config.UPLOAD_FOLDER
app.config["JWT_SECRET_KEY"] = config.SECRET_KEY

db.init_app(app)
marsh.init_app(app)

migrate = Migrate(app, db, render_as_batch=True)
jwt = JWTManager(app)

import errors
import routes.auth
import routes.translation