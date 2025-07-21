import os
import config
import jwt
import uuid

from app import app
from schemas import translations_schema, translation_schema
from flask import request, flash, jsonify
from werkzeug.utils import secure_filename
from models import Translation, User
from datetime import datetime
from db import db
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

ALLOWED_EXTENSIONS = ['srt']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@jwt_required()
@app.route('/translation', methods=['GET'])
def get_all_translations():
    user_id = get_jwt_identity()
    translations = Translation.query.filter_by(user_id=user_id)
    result = translations_schema.dump(translations)
    return jsonify(
        data=result), 200

@jwt_required
@app.route('/translation/<id>', methods=['GET'])
def get_translation(id : str):
    user_id = get_jwt_identity()
    user = User.query.filter_by(id = user_id).first()
    translation = Translation.query.filter_by(id=id).first()

    if translation in user.translations:
        result = translation_schema.dump(translation)
        return result, 200

    return jsonify(error="This translation belongs to another user"), 401

@jwt_required()
@app.route('/translation', methods=['POST'])
def create_new_translation():

    user_id = get_jwt_identity()
    user = User.query.filter_by(id = user_id).first()

    if 'file' not in request.files:
        return (jsonify(error='No file part'), 400)

    file = request.files['file']

    if file.filename == '':
        return (jsonify(error='No file part'), 400)

    if file and allowed_file(file.filename):
            try:
                storage_ref = uuid.uuid4().hex + '.srt'
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], storage_ref))
                new_translation = Translation(
                    storage_ref = storage_ref,
                    filename = secure_filename(file.filename),
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
