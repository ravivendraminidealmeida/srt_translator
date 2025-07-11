from app import db

class Translation(db.Model):
    __tablename__ = "translation"

    id = db.Column(db.Integer, primary_key=True)
    download_link = db.Column(db.String)