# A function called make_snippet that takes a string as an argument and 
# returns the first five words and then a '...' if there are more than that.

class Snippet:
    def __init__(self):
        self.string = None
    def make_snippet(self, string):
        listOfWords = string.split()
        if len(listOfWords) >= 5:
            first_five_words = listOfWords[:5]
            result = ' '.join(first_five_words)
            result += "..."
            print(result)
            return result
        else:
            raise Exception("You have few words")



