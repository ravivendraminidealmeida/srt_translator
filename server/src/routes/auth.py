import config
import jwt

from app import app
from db import db
from models import User
from flask import request, abort, jsonify
from werkzeug.exceptions import HTTPException
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token, verify_jwt_in_request

@app.before_request
def auth_middleware():
    print(request.endpoint)
    if request.endpoint not in config.UNPROTECTED_ENDPOINTS:
        verify_jwt_in_request()

@app.route('/auth/signup', methods=['POST'])
def signup():
    email = request.json.get('email')
    pwd = request.json.get('password')
    username = request.json.get('username')

    if None in [pwd, username, email]:
        return(jsonify({"error": "Fields can not be null"}), 400)

    if User.query.filter_by(email = email).first() is not None:
        return(jsonify({"error": "A user with these informations already exists"}), 400)

    user = User(email = email, username = username)
    user.hash_password(password=pwd)

    try:
        db.session.add(user)
        db.session.commit()

        return \
        (
            jsonify(
                {
                    'email': user.email, 
                    'username': user.username,
                }
            ), 201
        )
    except:
        return (jsonify({"error": "There has been an error while creating the user"}, 500))

@app.route('/auth/login', methods=['POST'])
def login():
    email = request.json.get('email')
    pwd = request.json.get('password')

    if None in [email, pwd]:
        return \
            (jsonify({"error": "Email and password are required for login"}), 400)

    user = User.query.filter_by(email = email).first()

    if user.verify_password(pwd):
        access_token = create_access_token(identity=str(user.id))
        return jsonify(
            {
                "token": access_token,
            }
        )
    
    return (jsonify(error="Invalid credentials"), 401)