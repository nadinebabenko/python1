#Ask a user for a word
#Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

#Make sure the letters are the keys.
#Make sure the letters are strings.
#Make sure the indexes are stored in a list and those lists are values.
word = input("Enter a word: ")
letter_dict = {}

for i, letter in enumerate(word):
    if letter not in letter_dict:
        letter_dict[letter] = [i]
    else:
        letter_dict[letter].append(i)

print(letter_dict)

#Challenge 2
#Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
#Sort the list in alphabetical order.
#Return “Nothing” if you can’t afford anything from the store.

wallet = float(input("How much money do you have in your wallet? "))

store_items = {
    "banana": 4.5,
    "nuts": 15.25,
    "mamtakim": 20.75,
    "grapes": 1.0,
    "tost with salmon": 24.8
}

affordable_items = []

for item, price in store_items.items():
    if price <= wallet:
        affordable_items.append(item)

if affordable_items:
    affordable_items.sort()
    print("You can afford the following items:")
    for item in affordable_items:
        print("- " + item)
else:
    print("Nothing")