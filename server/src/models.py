from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from passlib.apps import custom_app_context as pwd_context
from db import db

class User(db.Model):
   __tablename__ = "user" 
   id = Column(Integer, primary_key=True)
   username = Column(String)
   email = Column(String)
   _password_hash = Column(String)
   translations = relationship("Translation")

   def hash_password(self, password):
    self._password_hash = pwd_context.encrypt(password)

   def verify_password(self, password):
    return pwd_context.verify(password, self._password_hash)


class Translation(db.Model):
    __tablename__ = "translation"
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    storage_ref = Column(String)
    download_link = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey("user.id"))
    
    
    