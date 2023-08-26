#Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
        
        
    def __str__(self):
        return f"{self.amount} {self.currency}"
    
    def __int__(self):
        return self.amount
    
    def __repr__(self):
        return f"{self.amount} {self.currency}"
    
    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        else:
            raise TypeError(f"Cannot add between Currency type and {type(other)}")
    
    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, int):
            self.amount += other
        else:
            raise TypeError(f"Cannot add between Currency type and {type(other)}")
        return self
    
#Exercise 2: Import
#func.py
def add_numbers(num1, num2):
    result = num1 + num2
    print(result)

    # exercise_one.py
from func import add_numbers

add_numbers(5, 7)

#Exercise 3: Random Module
import random

def roll_dice(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Congratulations! You rolled the same number!")

#Exercise 4: String Module
import string
import random

def generate_random_string():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(5))

# Exercise 5 : Current Date
import datetime

def display_current_date():
    current_date = datetime.datetime.now()
    print(current_date.strftime("%Y-%m-%d"))

    #Exercise 6 : Amount Of Time Left Until January 1st
    import datetime

def time_left_until_january_first():
    now = datetime.datetime.now()
    january_first = datetime.datetime(now.year + 1, 1, 1)
    time_left = january_first - now
    print(f"The 1st of January is in {time_left.days} days and {time_left.seconds // 3600}:{(time_left.seconds // 60) % 60}:{time_left.seconds % 60} hours.")

    #7 : Birthday And Minutes
from datetime import datetime

def minutes_lived(birthdate):
    birth_datetime = datetime.strptime(birthdate, '%Y-%m-%d')
    now_datetime = datetime.now()
    minutes_lived = (now_datetime - birth_datetime).total_seconds() // 60
    return f"You have lived for {minutes_lived} minutes."

birthdate = '1994-07-08'
print(minutes_lived(birthdate))

#Exercise 8 : Faker Module
from faker import Faker
fake = Faker()
users = []
def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)