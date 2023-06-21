
class TextRead:
    def __init__(self, string):
        self.string = string
    def estimate_reading_time(self):
        words = self.string.split(" ")
        reading_time = len(words)/200
        return reading_time
    


