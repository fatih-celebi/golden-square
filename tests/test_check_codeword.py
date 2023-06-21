from lib.check_codeword import *

# If the word "horse" it should return "Correct! Come in." 

def test_check_codeword_returns_CorrectComeIn_for_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

# If the first letter "h" and the last letter is "e"  it should return Close, but nope."

def test_check_codeword_returns_Closebutnope_for_h_and_e():
    result = check_codeword("hadie")
    assert result == "Close, but nope."

# If the word "Horse" it should return "WRONG!"

def test_check_codeword_returns_wrong_for_wrong_word():
    result = check_codeword("polly")
    assert result == "WRONG!"