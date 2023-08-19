#Exercise 1 : Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def walk(self):
        return f'{self.name} is gracefully walking around'

    def meow(self):
        return 'Meow!'
    
all_cats = [
    Bengal('Benny', 4),
    Chartreux('Dima', 8),
    Siamese('lion', 5, 'brown'),
]
sara_pets = Pets(all_cats)
sara_pets.walk()


# Exercise 2 : Dogs
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} won the fight"
        else:
            return f"{other_dog.name} won the fight"

dog1 = Dog("Max", 3, 20)
dog2 = Dog("Buddy", 5, 25)
dog3 = Dog("Rocky", 2, 15)

print(dog1.bark())
print(dog2.run_speed())

#Exercise 3 : Dogs Domesticated
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} won the fight"
        else:
            return f"{other_dog.name} won the fight"

dog1 = Dog("Max", 3, 20)
dog2 = Dog("Buddy", 5, 25)
dog3 = Dog("Rocky", 2, 15)

print(dog1.bark())
print(dog2.run_speed())

import random
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *dog_names):
        print(f"{', '.join(dog_names)} all play together")
    
    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            trick = random.choice(tricks)
            print(f"{self.name} {trick}")
        else:
            print(f"{self.name} is not trained yet")