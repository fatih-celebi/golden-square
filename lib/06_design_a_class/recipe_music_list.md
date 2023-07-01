# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
class MusicList():
    def add(self, music):
    # Parameter: 
    # String, representing music name
    pass

    def list_of_all_musics(self):
    # returns
    # a list of all musics
    pass



```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
Initially there are no music
It should return => []
"""
music = MusicList()
music.list_of_all_musics() # => []

"""
After adding a music 
It should return the music in a list

"""
music = MusicList()
music.add("Sorry")
music.list_of_all_musics() # => ["Sorry"]

"""
After adding multiple musics 
It should return all the musics in a list

"""
music = MusicList()
music.add("Sorry")
music.add("Ok, Next")
music.add("Hello")
music.list_of_all_musics() # => ["Sorry", "Ok, Next", "Hello"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!