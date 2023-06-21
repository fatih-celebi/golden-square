from lib.gratitudes import *

def test_gratitudes_format():
    gratitudes = Gratitudes()
    gratitudes.add("Family")
    gratitudes.add("Health")
    formatted = gratitudes.format()
    assert formatted == "Be grateful for: Family, Health"
