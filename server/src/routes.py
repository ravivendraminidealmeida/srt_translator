from app import app
from models import Translation

@app.route("/")
def index():
    return Translation.query.all()
