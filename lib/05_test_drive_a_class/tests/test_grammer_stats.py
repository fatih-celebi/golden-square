import pytest
from lib.grammer_stats import GrammarStats


def test_if_text_starts_with_capital_letter():
    text = GrammarStats()
    result = text.check("fatih.")
    assert result == False

    result = text.check("Fatih.")
    assert result == True


def test_if_text_ends_with_punctuation():
    text = GrammarStats()
    result = text.check("Fatih")
    assert result == False

    result = text.check("Fatih.")
    assert result == True

def test_percentage_good():
    text = GrammarStats()
    assert text.percentage_good() == 0  # No texts checked yet
  
    text.check("Hello, World!")  # Passes grammar check
    assert text.percentage_good() == 100  # 1 out of 1 text passed (100%)
  
    text.check("Hey there!")  # Passes grammar check
    assert text.percentage_good() == 100  # 2 out of 2 texts passed (100%)
  
    text.check("Incomplete sentence")  # Fails grammar check
    assert text.percentage_good() == 66  # 2 out of 3 texts passed (66%)
