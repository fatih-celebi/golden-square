import pytest

from lib.task_tracker import *


"""
There are no tasks
"""
def test_initially_has_no_tasks():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []

"""
When we add a task 
It iis reflected ub the list of tasks
"""
def test_add_task_reslected_in_tasks():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    assert tracker.list_incomplete() == ["Walk the dog"]

"""
When we add multiple tasks
It is reflected ub the list of tasks
"""
def test_add_multiple_tasks():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Walk the cat")
    tracker.add("Walk the frog")
    assert tracker.list_incomplete() == ["Walk the dog", "Walk the cat", "Walk the frog"]


"""
When we add multiple tasks
And mark one as complete
It disappears from the list of tasks
"""
def test_mark_as_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Walk the cat")
    tracker.add("Walk the frog")
    tracker.mark_complete(1)
    assert tracker.list_incomplete() == ["Walk the dog", "Walk the frog"]

"""
When we try to mark a test that does not exists
It raises an error
"""

def test_mark_task_that_is_too_high_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(2) 
    assert str(err.value) == "No such task to mark as completed"
    assert tracker.list_incomplete() == ["Walk the dog"]

