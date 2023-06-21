from lib.make_snippet import *

# "nebiat fatih charlotte sam jon john jane"
# ==> "nebiat fatih charlotte sam jon"

def test_returns_the_first_five_words():
    word = Snippet()
    result = word.make_snippet("nebiat fatih charlotte sam jon john jane")
    result = result.replace(".", "")
    assert result == "nebiat fatih charlotte sam jon"


def test_returns_adding_ellipsis_at_the_end():
    word = Snippet()
    result = word.make_snippet("nebiat fatih charlotte sam jon john jane")
    assert result == "nebiat fatih charlotte sam jon..."
