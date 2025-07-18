from app import app
from db import db
from models import User
from flask import request, abort, jsonify
from werkzeug.exceptions import HTTPException
from datetime import datetime, timedelta
import config
import jwt

@app.route('/auth/me', methods=['GET'])
def get_current_user():
    pass

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

    if not user:
        return (jsonify(error="Invalid credentials"), 401)

    if user.verify_password(pwd):

        hours_to_expire = int(config.TOKEN_EXPIRATION_TIME_IN_HOURS)


        token = jwt.encode(
            {
                "username": user.username,
                "email": user.email,
                "expiration_time": datetime.isoformat(datetime.now() + timedelta(hours=hours_to_expire)) 
            },
            algorithm="HS256",
            key=config.SECRET_KEY
        )
        return jsonify(
            {
                "token": token,
                "expires_in": int(timedelta(hours=hours_to_expire).total_seconds())
            }
        )
    
    return (jsonify(error="Invalid credentials"), 401)