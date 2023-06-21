import pytest
from lib.password_checker import *

# def test_if_length_is_correct():
#     password = PasswordChecker()
#     result = password.check("123456789")
#     assert result == True


def test_if_sending_error_message():
    password = PasswordChecker()
    with pytest.raises(Exception) as error:
        password.check("1234")
    error_message = str(error.value)
    assert error_message == "Invalid password, must be 8+ characters."

        