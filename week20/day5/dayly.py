#Answer the following questions

#Answer the following questions

#What is a class?
#In object-oriented programming, a class is a blueprint for creating objects. It defines a set of attributes and methods that the objects of that class will have. Attributes are the data members (variables) and methods are the functions that operate on those data members. Classes provide a 
# way to organize and encapsulate related data and behavior, making code more modular and reusable.


#What is an instance?
#An instance is an object of a particular class. For example, if we have a class called Person, an instance of that class would be a person object. We can create as many instances of a class as we want.

#What is encapsulation?
#Encapsulation is one of the fundamental concepts of object-oriented programming. It refers to the practice of hiding the internal details of an object and providing a public interface for interacting with it. This means that the implementation details of an object are kept private, and can only be accessed through methods that are part of the object's public interface. Encapsulation helps to ensure that the object's internal state remains consistent and that it can only be modified in a controlled way. It also helps to prevent external code from accidentally or maliciously modifying the object's state.


#What is abstraction?
#Abstraction is a fundamental concept in object-oriented programming that refers to the process of reducing complexity by hiding unnecessary details while highlighting essential features. It involves creating a simplified representation of a complex system that includes only the most relevant information. In programming, abstraction is achieved through the use of abstract classes and interfaces, which define a set of methods that must be implemented by concrete classes.


#What is inheritance?
#Inheritance is a fundamental concept in object-oriented programming that allows one class to inherit properties and methods from another class. The class that is being inherited from is called the parent class or superclass, and the class that is inheriting is called the child class or subclass. The child class can access all the public and protected members of the parent class, and can also override or extend the behavior of those members. Inheritance helps to promote code reuse, reduce code duplication, and create a more modular and organized codebase.


#What is multiple inheritance?
#Multiple inheritance is a feature of object-oriented programming that allows a class to inherit properties and methods from multiple parent classes. In other words, a child class can have more than one parent class. This allows for greater code reuse and flexibility, as it allows a class to combine the functionality of multiple classes. However, multiple inheritance can also lead to increased complexity and potential conflicts, as it can be difficult to manage the interactions between multiple parent classes. As a result, it is important to use multiple inheritance judiciously and to carefully consider the design of the class hierarchy.



#What is polymorphism?

#Polymorphism is a fundamental concept in object-oriented programming that refers to the ability of objects of different classes to be used interchangeably. In other words, it allows objects of different types to be treated as if they were of the same type. This is achieved through the use of inheritance and interfaces, which allow different classes to share common methods and properties. Polymorphism helps to promote code reuse, reduce code duplication, and create a more modular and flexible codebase. It is a key feature of many programming languages, including Python.

#What is method resolution order or MRO?
#Method Resolution Order (MRO) is the order in which a programming language searches for methods and attributes in a class hierarchy. In Python, MRO is determined by the C3 linearization algorithm, which is used to resolve conflicts that arise when a class inherits from multiple parent classes. The MRO defines the order in which Python looks for methods and attributes in a class hierarchy, starting with the current class, then its parent classes, and so on, until it reaches the top-level object class. This allows Python to resolve method and attribute names in a consistent and predictable way, even in complex class hierarchies. Understanding MRO is important for writing correct and efficient Python code, especially when working with multiple inheritance.



#Create A Deck Of Cards Class.
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop()