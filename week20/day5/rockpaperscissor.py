from game import Game 
def get_user_menu_choice():
    """
    Displays a menu 
    """
    while True:
        print("Menu:")
        print("1. Play a new game")
        print("2. Show scores")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


def print_results(results):
    """
    Prints the results of the games played.
    Takes a dictionary of the results of the games played.
    """
    print("Results:")
    print(f"Win: {results['win']}")
    print(f"Loss: {results['loss']}")
    print(f"Draw: {results['draw']}")
    print("Thank you for playing!")

def main():
    """
    The main function.
    Displays the menu repeatedly until the user types in the value to exit the program.
    When the user chooses to play a game, creates a new Game object and calls its play() function.
    Remembers the results of every game that is played.
    """
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "1":
       
                
            # Create a new Game object and call its play() function
            # Receive the result of the game that is returned
            pass
        elif choice == "2":
             
            print_results(results)
        elif choice == "3":
            # Call the print_results function to display a summary of all the games played
            print_results(results)
            break 
get_user_menu_choice()
game = Game()
result = game.play()
 


     



 
 