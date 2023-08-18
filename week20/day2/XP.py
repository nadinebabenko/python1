 #Exercise 1: Cats
#Instantiate three Cat objects using the code provided above.
#Outside of the class, create a function that finds the oldest cat and returns the cat.
#Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age  

cat1 = Cat("Malfoy", 3)
cat2 = Cat("Fluffy", 6)
cat3 = Cat("Germy", 8)

def find_oldest_cat(*cats):
    oldest_cat = None
    for cat in cats:
        if oldest_cat is None or cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and  he is {oldest_cat.age} years old.")

# Exercise 2 : Dogs
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

davids_dog = Dog("Rex", 50)
print(f"David's dog is named {davids_dog.name} and is {davids_dog.height}cm tall.")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height}cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger.")
else:
    print(f"{sarahs_dog.name} is bigger.")

#Exercise 3 : Who’s The Song Producer?
# a class called Song, it will show the lyrics of a song.
#Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
#Create an object, for example:

#stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway = Song(["We all live in a yellow submarine", "Yellow submarine, yellow submarine", "We all live in a yellow submarine", "Yellow submarine, yellow submarine"])
stairway.sing_me_a_song()

#Exercise 4 : Afternoon At The Zoo 
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        animal_dict = {}
        for animal in self.animals:
            if animal[0] not in animal_dict:
                animal_dict[animal[0]] = [animal]
            else:
                animal_dict[animal[0]].append(animal)
        sorted_animals = sorted(animal_dict.items())
        for key, value in sorted_animals:
            print(key + ": ", end="")
            print(", ".join(value))

    def get_groups(self):
        animal_dict = {}
        for animal in self.animals:
            if animal[0] not in animal_dict:
                animal_dict[animal[0]] = [animal]
            else:
                animal_dict[animal[0]].append(animal)
        for key, value in animal_dict.items():
            print(key + ": ", end="")
            print(", ".join(value))

# Create an object called ramat_gan_safari and call all the methods
ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Eel")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()