from flask import Flask
from flask import jsonify
from backend_epithet_generator.helpers import EpithetGenerator
from backend_epithet_generator.helpers import Vocabulary

app = Flask(__name__)


@app.route('/')
def generate_epithets():
    result = EpithetGenerator().select_words()
    return jsonify({'epithets': result})


@app.route('/vocabulary')
def vocabulary():
    result = Vocabulary().read_json()
    return jsonify({'vocabulary': result})


@app.route('/epithets/<int:num>')
def generate_multiple_epithets(num):
    result = EpithetGenerator().generate(num)
    return jsonify({'epithets': result})

@app.route('/epithets/random')
def random_route():
    result = EpithetGenerator().