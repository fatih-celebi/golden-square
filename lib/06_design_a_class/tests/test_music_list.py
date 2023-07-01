import pytest
from lib.music_list import *

"""
Initially there are no music
It should return => []
"""
def test_initially_returns_empty():
    music = MusicList()
    assert music.list_of_all_musics() == []

"""
After adding a music 
It should return the music in a list

"""
def test_add_one_music_to_the_list():
    music = MusicList()
    music.add("Sorry")
    assert music.list_of_all_musics() == ["Sorry"]

"""
After adding multiple musics 
It should return all the musics in a list

"""
def test_add_multiple_musics_to_the_list():
    music = MusicList()
    music.add("Sorry")
    music.add("Ok, Next")
    music.add("Hello")
    music.list_of_all_musics() # => ["Sorry", "Ok, Next", "Hello"]