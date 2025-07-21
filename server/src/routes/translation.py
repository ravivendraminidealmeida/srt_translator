import os
import config
import jwt
import uuid

from app import app
from schemas import translations_schema, translation_schema
from flask import request, jsonify
from werkzeug.utils import secure_filename
from models import Translation, User
from datetime import datetime
from db import db
from flask_jwt_extended import jwt_required, get_jwt_identity 
from celery.result import AsyncResult
from tasks import schedule_translation

ALLOWED_EXTENSIONS = ['srt']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
@app.route('/translation', methods=['GET'])
def get_all_translations():
    user_id = get_jwt_identity()
    translations = Translation.query.filter_by(user_id=user_id)
    result = translations_schema.dump(translations)
    return jsonify(data=result), 200

@app.route('/translation/<id>', methods=['GET'])
def get_translation(id : str):
    user_id = get_jwt_identity()
    user = User.query.filter_by(id = user_id).first()
    translation = Translation.query.filter_by(id=id).first()

    if translation in user.translations:
        result = translation_schema.dump(translation)
        return result, 200

    return jsonify(error="This translation belongs to another user"), 401

@app.route('/translation', methods=['POST'])
def create_new_translation():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id = user_id).first()
    data = request.form

    if 'file' not in request.files:
        return (jsonify(error='No file part'), 400)

    file = request.files['file']

    if file.filename == '':
        return (jsonify(error='No file part'), 400)

    if file and allowed_file(file.filename):
        try:
            storage_ref = uuid.uuid4().hex + '.srt'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], storage_ref))

            from_lang = data.get("from_lang")
            to_lang = data.get("to_lang")
            new_translation = Translation(
                original_storage_ref = storage_ref,
                filename = secure_filename(file.filename),
                download_link = None,
                created_at = datetime.now(),
                updated_at = None,
                user_id = user.id,
                from_lang = from_lang if from_lang else config.DEFAULT_FROM_LANG,
                to_lang = to_lang if to_lang else config.DEFAULT_TO_LANG
            )
            db.session.add(new_translation)
            db.session.commit()
            schedule_translation(new_translation.id)
            return jsonify({"message": "The file was successfully uploaded"}), 200
        except:
            return jsonify({"error": "There has been an error during the upload proccess"}), 500

    return jsonify({"error": f"Only {ALLOWED_EXTENSIONS} files are allowed"}), 400
