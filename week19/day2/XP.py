#Exercise 1 : What Are You Learning ?

def display_message():
    print("In this chapter, I'm learning about functions in Python and how they are used.")

display_message()

#Exercise 2: What’s Your Favorite Book ? 
def favorite_book(title):
    print("One of my favorite books is " + title)

favorite_book("Harry Potter")

#Exercise 3: Some Geography 
 
def describe_city(city="Tel Aviv", country = "Israel"):
    print(city + " is in " + country)

describe_city()

#Exercise 4 : Random
 
import random
def generate_random_number(n):
    if n < 1 or n > 100:
        print("Number must be between 1 and 100")
    else:
        random_number = random.randint(1, 100)
        print("Random number between 1 and 100:", random_number)
        if n == random_number:
            print("Success! The numbers match.")
        else:
            print("Fail! The numbers do not match.")
            print("Your number:", n)
            print("Random number:", random_number)
generate_random_number(50)

#Exercise 5 : Let’s Create Some Personalized Shirts !
 
def make_shirt(size="large", text="I love Python"):
    print("The size of the shirt is " + size + " and the text is " + text)
 
make_shirt()

# Make medium shirt with the default message
def make_shirt2 (size="medium",text="I love dogs"):
    print("The size of the shirt is " + size + " and the text is " + text)
make_shirt2()

# Make a shirt of any size with a different message
def make_shirt3(size="small", text="Python is awesome!"):
    print("The size of the shirt is " + size + " and the text is " + text)
make_shirt3()
 

 #Exercise 6 : Magicians …

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
#Pass the list to a function called show_magicians(), which prints the name of each magician in the list.

def show_magicians(magician_names):
    for name in magician_names:
        print(name)

#Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
def make_great():
    great_magicians = []
    while magician_names:
        magician = magician_names.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        magician_names.append(great_magician)
    return magician_names

make_great()
show_magicians()
 

 