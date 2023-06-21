from lib.greet import *

def test_greet_returns_HelloFatih_for_Fatih():
    result = greet("Fatih")
    assert result == "Hello, Fatih!"
