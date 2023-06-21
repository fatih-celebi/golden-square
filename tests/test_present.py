import pytest
from lib.present import *

def test_wrap():
    present = Present()
    present.wrap(12)
    assert present.unwrap() == 12

def test_if_already_wrapped():
    present = Present()
    present.wrap(2)
    with pytest.raises(Exception) as error:
        present.wrap(7)
        error_message = str(error.value)
        assert error_message == "A contents has already been wrapped."

def test_if_no_contents_have_been_wrapped():
    present = Present()
    with pytest.raises(Exception) as error:
        present.unwrap()
        error_message = str(error.value)
        

def test_wrapping_already_wrapped_value():
    present = Present()
    present.wrap(76)
    with pytest.raises(Exception) as error:
        present.wrap(5)
        assert present.unwrap() == 76