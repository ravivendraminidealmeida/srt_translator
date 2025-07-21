import pysrt
import config
import uuid
import os

from celery import shared_task
from deep_translator import GoogleTranslator 
from models import Translation
from db import db

@shared_task
def schedule_translation(
        translation_id : int
    ):
    
    translation = Translation.query.filter_by(id=translation_id).first()
    translator = GoogleTranslator(
        source=translation.from_lang,
        target=translation.to_lang
    )
    subs = pysrt.open(os.path.join(config.UPLOAD_FOLDER, translation.original_storage_ref))
    translated = translator.translate_batch([sub.text for sub in subs])
    
    for translated_text, sub in zip(translated, subs):
        sub.text = translated_text
    
    if subs is not None:
        translated_storage_ref = os.path.join(config.UPLOAD_FOLDER, uuid.uuid4().hex)
        subs.save(
            path=translated_storage_ref,
            encoding='utf-8'
        ) 
        translation.translated_storage_ref = translated_storage_ref
        db.session.commit()
        
        
        
        