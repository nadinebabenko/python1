#Challenge 1 : Sorting
#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Use List Comprehension
words = input("Enter comma separated words: ").split(",")
sorted_words = sorted(words)
result = ",".join(sorted_words)
print(result)

#Challenge 2 : Longest Word
#Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest.strip(",.?!;:'\"")

sentence = input("Enter a sentence: ")
result = longest_word(sentence)
print(result)

sentence = "Nadya is going to work in a good Itech company"
result = longest_word(sentence)
print(result)