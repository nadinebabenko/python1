import random
from rockpaperscissor   import get_user_menu_choice
from rockpaperscissor   import print_results
from rockpaperscissor   import main

class Game:
    def get_user_item(self):
        while True:
            user_item = input("Select an item (rock/paper/scissors): ")
            if user_item.lower() in ["rock", "paper", "scissors"]:
                return user_item.lower()
            else:
                print("Invalid input. Please select rock, paper, or scissors.")

    def get_computer_item(self):
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or (user_item == "paper" and computer_item == "rock") or (user_item == "scissors" and computer_item == "paper"):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"You selected {user_item}. The computer selected {computer_item}. You {result}!")
        return result + ";"

 