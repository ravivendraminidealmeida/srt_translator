from app import app
from db import db
from models import User
from flask import request, abort, jsonify


@app.route('/auth/me', methods=['GET'])
def get_current_user():
    pass

@app.route('/auth/signup', methods=['POST'])
def signup():
    email = request.json.get('email')
    pwd = request.json.get('password')
    username = request.json.get('username')

    if None in [pwd, username, email]:
        abort(400)

    if User.query.filter_by(email = email).first() is not None:
        abort(400)

    user = User(email = email, username = username)
    user.hash_password(password=pwd)

    db.session.add(user)
    db.session.commit()

    return \
        jsonify(
            {
                'email': user.email, 
                'username': user.username,
            }
        ) 

@app.route('/auth/login', methods=['POST'])
def login():
    pass

