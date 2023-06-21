from lib.string_builder import *

def test_returns_updated_string():
    string = StringBuilder()
    string.add("nil")
    result = string.output()
    assert result == "nil"


def test_returns_length_of_string():
    string = StringBuilder()
    string.add("ada")
    result = string.size()
    assert result == 3