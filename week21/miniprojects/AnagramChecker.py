class AnagramChecker:
    def __init__(self, sowpods_txt):
        with open('sowpods.txt', 'r') as f:
            self.sowpods = set(f.read().split())

    def is_valid_word(self, word):
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        word = word.lower()
        anagrams = []
        for w in self.word_list:
            if self.is_anagram(word, w) and word != w.lower():
                anagrams.append(w)
        return anagrams
anagram_checker = AnagramChecker('sowpods.txt')
if anagram_checker.is_valid_word('ABATTISES'):
    print(anagram_checker.get_anagrams('hello'))
else :
    print("not valid word")
