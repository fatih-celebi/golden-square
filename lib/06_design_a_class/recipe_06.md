# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
class TaskTracker():
    def add(self, task):
        #Parameters:
        #Task: string, representing a task
        pass

    def list_incomplete(self):
        #Returns
        #A list of incomplete tasks
        pass
    
    def mark_complete(self):
        #Parameters:
        #Task: string, representing a task
        pass

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
There are no tasks
"""
tracker = TaskTracker()
tracker.list_incomplete() # => []

"""
When we add a task 
It iis reflected ub the list of tasks
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.list_incomplete() # => ["Walk the dog"]

"""
When we add multiple tasks
It iis reflected ub the list of tasks
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.add("Walk the frog")
tracker.list_incomplete() # => ["Walk the dog", "Walk the frog"]

"""
When we add multiple tasks
And mark one as complete
It disappears from the list of tasks
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.add("Walk the cat")
tracker.add("Walk the frog")
tracker.mark_complete(1)
tracker.list_incomplete() # => ["Walk the dog", "Walk the frog"]

"""
When we try to mark a test that does not exists
It raises an error
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.mark_complete(2) # => Raises an error "No such task to mark as completed"
tracker.list_incomplete() # => ["Walk the dog"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!