#Save it in your development directory. Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?
import random
def get_words_from_file(wordlist):
    with open('wordlist.txt', 'r') as file:
        words = file.read().split()
    return words
 

def get_random_sentence(length):
    words = get_words_from_file("wordlist.txt")
    sentence = " ".join(random.sample(words, length)).lower() + "."
    return sentence

def main():
    print("This program generates a random sentence.")
    length = input("How long do you want the sentence to be (2-20)? ")
    try:
        length = int(length)
        if length < 2 or length > 20:
            raise ValueError
    except ValueError:
        print("Error: Please enter an integer between 2 and 20.")
        return
    sentence = get_random_sentence(length)
    print(sentence)

if __name__ == "__main__":
    main()

 #Exercise 2: Working With JSON
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
sampleDict = json.loads(sampleJson)
salary = sampleDict["company"]["employee"]["payable"]["salary"]
print(salary)
sampleDict["company"]["employee"]["birth_date"] = "1994-07-08"
print(sampleDict)
#with open("output.json", "w") as outfile:
    #json.dump(sampleDict, outfile)