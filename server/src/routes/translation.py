from app import app

@app.route('/translation', methods=['POST'])
def new_translation():
    pass

@app.route('/translation/<id>', methods=['GET'])
def get_translation(id : str):
    return id