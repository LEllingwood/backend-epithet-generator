from flask import Flask
from tinydb import Tinydb

app = Flask(__name__)
db = Tinydb('data.json')


@app.route('/')
def generate_epithets():
    # function that randomly generates epithets
    # return {'epithets':{}}
    pass

@app.route('/vocabulary')
def vocabulary():
    # function used to serve the vocabulary to the generate epithets function
    # return {'vocabulary': {}}
    pass

