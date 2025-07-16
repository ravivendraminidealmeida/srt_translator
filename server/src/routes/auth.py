from app import app
from db import db
from models import User
from flask import request, abort, jsonify
from werkzeug.exceptions import HTTPException

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
    pass

