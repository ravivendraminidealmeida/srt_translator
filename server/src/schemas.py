from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from flask_marshmallow import Marshmallow
from models import Translation

marsh = Marshmallow()

class TranslationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Translation
        include_relationships = True
        load_instance = True
        fields = (
            "id", 
            "filename",
            "download_link",
            "created_at"
        )
        
translations_schema = TranslationSchema(many=True)  
translation_schema = TranslationSchema()