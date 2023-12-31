class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception ("Diary entries must have a title and contents")
        self._title = title
        self._contents = contents
        self._read_so_far = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self._title}: {self._contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        words = self.format().split(" ")
        return len(words)

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Cannot calculate reading time with wpm of 0")
        contents_word_count = len(self._contents.split())
        return contents_word_count / wpm

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        words_user_can_read = wpm * minutes
        words = self._contents.split()
        chunk_start = self._read_so_far
        chunk_end = self._read_so_far + words_user_can_read
        chunk_words = words[chunk_start:chunk_end]

        self._read_so_far = chunk_end
        return " ".join(chunk_words)
