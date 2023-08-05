#Exercise 1 : Temperature Advice
import random

import random

def get_random_temp(season):
    if season == 'winter':
        return random.randint(-10, 16)
    elif season == 'summer':
        return random.randint(16, 40)
    elif season == 'autumn' or season == 'fall':
        return random.randint(0, 23)
    elif season == 'spring':
        return random.randint(5, 23)
    else:
        raise ValueError('Invalid season')
get_random_temp('winter')

def main():
    season = input("Enter a season (summer, autumn, winter, spring): ")
    temp = get_random_temp(season)
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don't forget your coat.")
    elif temp < 24:
        print("Nice weather! Enjoy your day.")
    elif temp < 32:
        print("Getting hot! Stay hydrated.")
    else:
        print("Very hot! Stay indoors if possible.")

if __name__ == '__main__':
    main()

    #Exercise 2 : Star Wars Quiz
    data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
    
def ask_questions(data):
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []
    for question in data:
        user_answer = input(question["question"] + " ")
        if user_answer.lower() == question["answer"].lower():
            correct_answers += 1
        else:
            incorrect_answers += 1
            wrong_answers.append(question["question"])

   
ask_questions(data) 

def inform_user(correct_answers, incorrect_answers, wrong_answers):
    print("You got {} correct answers and {} incorrect answers.".format(correct_answers, incorrect_answers))
    if incorrect_answers > 0:
        print("The following questions were answered incorrectly:")
        for question in wrong_answers:
            print(question)
           
    inform_user(correct_answers, incorrect_answers, wrong_answers)
    
    print("Thanks for playing!")

    #Exercise 3 : When Will I Retire ? 
 

def get_age(year, month, day):
    current_year = 2023
    current_month = 8
    current_day = 5
    age = current_year - year
    if month > current_month:
        age -= 1
    elif month == current_month:
        if day > current_day:
            age -= 1
    return age 
get_age(1960, 7, 15)
 
def can_retire(gender, date_of_birth):
    year, month, day = date_of_birth
    age = get_age(year, month, day)
    if gender == "male":
        if age >= 67:
            return True
        else:
            return False
    elif gender == "female":
        if age >= 62:
            return True
        else:
            return False
    else:
        return False
can_retire("female", (1994, 7, 15))

#Exercise 4:

def calculate_sum(X):
    return X + int(str(X)*2) + int(str(X)*3) + int(str(X)*4)

calculate_sum(3)
 


 
    
 

