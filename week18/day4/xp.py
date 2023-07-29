# Exercise 1 : Set
my_fav_numbers={7, 14,  63}
my_fav_numbers.add(3)
my_fav_numbers.add(2)
my_fav_numbers.remove(63)
print(my_fav_numbers)

friend_fav_numbers={1,2,3,4}

our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercise 2 : Tuple
#tuples are immutable, you can concatenate them using the + operator. In this process, the original object remains unchanged, and a new object is created.

#Exercise 3: List

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")

basket.count("Apples")
 
basket.clear()
print(basket)

#Exercise 4: Floats
#Integers and floats are two different kinds of numerical data. An integer (more commonly called an int) is a number without a decimal point. A float is a floating-point number, which means it is a number that has a decimal place. Floats are used when more precision is needed.

import numpy as np
for i in np.arange(1.5, 5.5, 0.5):
    print(i, end=', ')
 
 # Exercise 5: For Loop
 #print out every element which has an even index.
 even_i = [] 
 for i in range(1,21):
        if i % 2 == 0:
            even_i.append(i)
print(even_i)

# Exercise 6 : While Loop
keep_going = True
while keep_going:
     name = input('Enter your name, or type quit to exit ')
     if name == "Nadya":
        keep_going = False

#Exercise 7: Favorite Fruits

fruit=[]
list_lenght=3
for i in range(list_lenght):   
    item= input('Enter your favorite fruit to buy: ')
    fruit.append(item) 
    print(fruit)


    itme2=[]
    list_lenght=1
    itme2=input('Enter your favorite fruit to buy: ')
    if itme2 == fruit[0]:
        print('You chose one of your favorite fruits! Enjoy!')


#Exercise 8: Who Ordered A Pizza ?prompt = "\nWhat topping would you like on your pizza?"

prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break

    #Exercise 9: Cinemax
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")

        #part2

age = input("How old are you? ")
age = int(age)

if age <  21:
    print("Sorry you couldnt watch the movie")
else:
    print("Great and welcome to the film")

    #Exercise 10 : Sandwich Orders
    
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")