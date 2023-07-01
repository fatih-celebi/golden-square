class GrammarStats:
    def __init__(self):
        self.total_checks = 0
        self.passed_texts = 0
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        self.total_checks += 1
        punctuation_marks = ".,;:!?"
        isCorrectGrammar = text[0].isupper() and text[-1] in punctuation_marks
        if isCorrectGrammar:
            self.passed_texts += 1

        return isCorrectGrammar


  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.total_checks == 0:
            return 0
        
        percentage = (self.passed_texts / self.total_checks) * 100
        return int(percentage)
        

text = GrammarStats()
