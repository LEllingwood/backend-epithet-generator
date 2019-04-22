import pytest
import json

from backend_epithet_generator.helpers import EpithetGenerator, Vocabulary
from backend_epithet_generator.app import app 


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
    # use assertion errors here.  
    with pytest.raises(AssertionError):
        assert isinstance(V.read_json(P), tuple)


# unit test the EpithetGenerator class:  
# # happy path 
def test_select_words_happy():
    assert len(E.select_words().split()) == 3


# # sad path
def test_select_words_sad():
    with pytest.raises(AssertionError):
        assert len(E.select_words().split()) == 5


# # happy path 
def test_generate_happy():
    assert len(E.generate(2)) == 2


# sad path
def test_generate_sad():
    with pytest.raises(AssertionError):
        assert len(E.generate(2)) == 5


# assertion test
def test_app():
    result = app.test_client().get('/')
    assert result.status_code == 200
    result = result.data.decode()
    assert isinstance(result, str)
    data = json.loads(result)
    assert isinstance(data, dict)
    assert data["epithets"]