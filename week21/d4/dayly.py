class Text:
    def __init__(self, text):
        self.text = text
    
    def word_frequency(self, word):
        words = self.text.split()
        frequency = words.count(word)
        if frequency == 0:
            return None
        else:
            return frequency
    
    def most_common_word(self):
        words = self.text.split()
        unique_words = set(words)
        most_common = None
        highest_frequency = 0
        for word in unique_words:
            frequency = words.count(word)
            if frequency > highest_frequency:
                highest_frequency = frequency
                most_common = word
        return most_common
    
    def unique_words(self):
        words = self.text.split()
        unique_words = set(words)
        return list(unique_words)
    
class Text:
    def __init__(self, text):
        self.text = text
    
    def word_frequency(self, word):
        words = self.text.split()
        frequency = words.count(word)
        if frequency == 0:
            return None
        else:
            return frequency
    
    def most_common_word(self):
        words = self.text.split()
        unique_words = set(words)
        most_common = None
        highest_frequency = 0
        for word in unique_words:
            frequency = words.count(word)
            if frequency > highest_frequency:
                highest_frequency = frequency
                most_common = word
        return most_common
    
    def unique_words(self):
        words = self.text.split()
        unique_words = set(words)
        return list(unique_words)
    
    @classmethod
    def from_file(cls, stranger):
        with open('stranger.txt', 'r') as f:
            text = f.read()
        return cls(text)
