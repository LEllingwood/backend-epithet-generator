from flask import Flask
from flask import jsonify
from helpers import EpithetGenerator
from helpers import Vocabulary

app = Flask(__name__)


@app.route('/')
def generate_epithets():
    result = EpithetGenerator().select_words()
    return jsonify({'epithets': result})


@app.route('/vocabulary')
def vocabulary():
    result = Vocabulary().read_json()
    return jsonify({'vocabulary': result})


@app.route('/epithets/<num>')
def generate_multiple_epithets():
    result = EpithetGenerator().generate()
    return jsonify({'epithets': result})

