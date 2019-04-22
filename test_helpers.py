from backend_epithet_generator.helpers import EpithetGenerator
from backend_epithet_generator.helpers import Vocabulary

E = EpithetGenerator()
V = Vocabulary
P = "resources/data.json"


# unit test the Vocabulary Class: 
# happy path:
def test_read_json_happy():
    assert isinstance(V.read_json(P), dict)
    # pass


# sad path:
def test_read_json_sad():
    assert isinstance(V.read_json(P), tuple)


# unit test the EpithetGenerator class:  
# # happy path 
def test_select_words_happy():
    assert len(E.select_words().split()) == 3


# # sad path
def test_select_words_sad():
    assert len(E.select_words().split()) == 5


# # happy path 
def test_generate_happy():
    assert len(E.generate(2)) == 2


# sad path
def test_generate_sad():
    assert len(E.generate(2)) == 5

