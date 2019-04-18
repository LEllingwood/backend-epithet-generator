from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def generate_epithets():
    return jsonify({'epithets':[]})

@app.route('/vocabulary')
def vocabulary():
    return jsonify({'vocabulary': {}})

