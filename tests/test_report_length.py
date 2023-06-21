from lib.report_length import *

def test_report_length_returns_8_for_string():
    result = report_length("test str")
    assert result == "This string was 8 characters long."