import os
from app import app
from flask import request, flash, jsonify
from werkzeug.utils import secure_filename
from models import Translation, User
from datetime import datetime
from db import db
import config
import jwt

ALLOWED_EXTENSIONS = ['srt']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/translation', methods=['POST'])
def require_new_translation():

    token = \
        jwt.decode(
            request.headers["Authorization"].replace("Bearer", ""),
            options={"verify_signature": False}, # TODO: FIX THIS BEFORE PROD FOR GOD'S SAKE
            algorithms=["HS256"]
        )

    user = User.query.filter_by(email=token["email"]).first()
    
    if 'file' not in request.files:
        return (jsonify(error='No file part'), 400)

    file = request.files['file']

    if file.filename == '':
        return (jsonify(error='No file part'), 400)

    if file and allowed_file(file.filename):
            try:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                new_translation = Translation(
                    filename = filename,
                    download_link = None,
                    created_at = datetime.now(),
                    updated_at = None,
                    user_id = user.id,
                )
                db.session.add(new_translation)
                db.session.commit()
                return jsonify({"message": "The file was successfully uploaded"}), 200
            except:
                return jsonify({"error": "There has been an error during the upload proccess"}), 500

    return jsonify({"error": f"Only {ALLOWED_EXTENSIONS} files are allowed"}), 400
    

@app.route('/translation/<id>', methods=['GET'])
def get_translation(id : str):
    # TODO: Impl this
    return id