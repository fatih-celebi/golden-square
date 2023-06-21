# As a user
# So that I can keep track of my tasks
# I want to check if a text includes the string #TODO.

from lib.check_todo_list import *

def test_check_todo_list_when_doesnt_include_TODO():
    result = check_todo("Hello World")
    assert result == False

def test_check_todo_when_includes_TODO():
    result = check_todo("Complete the challenge #TODO")
    assert result == True