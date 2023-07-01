import pytest
from lib.diary_entry import *

"""
Given a title and contents format returns formatted entry like
"My Title: These are contents"
"""

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Content")
    result = diary_entry.format()
    assert result == "My Title: Content"

"""
Given a title and a contents 
count_words returns the number of words
"""

def test_count_words_in_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Content")
    result = diary_entry.count_words()
    assert result == 3

def test_errors_on_empty_title_or_string():
    with pytest.raises(Exception) as err:
        DiaryEntry("", "")
    assert str(err.value) == "Diary entries must have a title and contents"

"""
Given a words per minute of 2
and text with 2 words
reading_time returns 1 minute
"""

def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.reading_time(2)
    assert result == 1

"""
Given a words per minute of 2
and text with 4 words
reading_time returns 2 minute
"""

def test_reading_time_with_two_wpm_and_four_words():
    diary_entry = DiaryEntry("My Title", "Some contents and more")
    result = diary_entry.reading_time(2)
    assert result == 2

"""
Given a words per minute of 2 
and text with 3 words
reading_time returns 1.5 minute
"""

def test_reading_time_with_two_wpm_and_three_words():
    diary_entry = DiaryEntry("My Title", "Some more contents")
    result = diary_entry.reading_time(2)
    assert result == 1.5

"""
Given a words per minute of 0
and text with 4 words
reading_time raises an Error
"""

def test_reading_time_with_zero_wpm_and_three_words():
    diary_entry = DiaryEntry("My Title", "Some more contents")
    with pytest.raises(Exception) as err:
        diary_entry.reading_time(0)
    assert str(err.value) == "Cannot calculate reading time with wpm of 0"

    """
    Given a contents of six words 
    and a wpm of 2 
    and a minutes of 2
    reading_chunk returns the first four words
    """

def test_reading_chunk_with_two_wpm_and_two_minutes():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"

    """
    Given a contents of six words 
    and a wpm of 2 
    and a minutes of 1
    first time reading_chunk returns "one two"
    second time reading_chunk returns "three four"
    third time reading_chunk returns "five six"
    """

def test_reading_chunk_with_two_wpm_and_one_minute_called_multiple_times():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"
   
    """
    Given a contents of six words 
    and a wpm of 2 
    and a minutes of 
    first time reading_chunk returns "one two"
    second time reading_chunk returns "three four"
    third time reading_chunk returns "five six"
    """

def test_reading_chunk_with_two_wpm_and_one_minute_called_multiple_times():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"