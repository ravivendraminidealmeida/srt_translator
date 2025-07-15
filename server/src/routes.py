from app import app
from models import Translation

@app.route('/translation/<id>')
def get_translation(id : str):
    return id