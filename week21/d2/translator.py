 
from googletrans  import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translator = Translator()

german_words = []
for word in french_words:
    translation = translator.translate(word, dest='de').text
    german_words.append(translation)

print(german_words)