from AnagramChecker import AnagramChecker

def get_user_input():
    while True:
        choice = input("Enter 'input' to input a word, or 'exit' to exit: ")
        if choice in ["input", "exit"]:
            return choice
        else:
            print("Invalid choice. Please enter 'input' or 'exit'.")

def validate_word(word):
    return word.isalpha()

def get_valid_word():
    while True:
        word = input("Enter a word: ").strip()
        if " " in word:
            print("Error: Please enter only one word.")
        elif not validate_word(word):
            print("Error: Please enter only alphabetic characters.")
        else:
            return word

def get_anagrams(word):
    checker = AnagramChecker()
    return checker.get_anagrams(word)

def display_results(word, anagrams):
    print(f"YOUR WORD: \"{word}\"")
    if validate_word(word):
        if AnagramChecker().is_valid_word(word):
            print("This is a valid English word.")
        else:
            print("This is not a valid English word.")
    else:
        print("This is not a valid word.")
    print("Anagrams for your word:", ", ".join(anagrams))

while True:
    choice = get_user_input()
    if choice == "exit":
        break
    else:
        word = get_valid_word()
        anagrams = get_anagrams(word)
        display_results(word, anagrams)