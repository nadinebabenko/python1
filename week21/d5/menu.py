class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        # save item to database
        pass

    def delete(self):
        # delete item from database
        pass

    def update(self, new_name, new_price):
        # update item in database
        pass

class MenuManager:
    @staticmethod
    def get_by_name(name):
        # get item from database by name
        pass

    @staticmethod
    def all():
        # get all items from database
        pass

def show_user_menu():
    while True:
        print("Program Menu:")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show the Menu")
        print("E - Exit the Program")

        user_input = input("Enter your choice: ").upper()

        if user_input == "V":
            # call view_item function
            pass
        elif user_input == "A":
            # call add_item_to_menu function
            pass
        elif user_input == "D":
            # call remove_item_from_menu function
            pass
        elif user_input == "U":
            # call update_item_from_menu function
            pass
        elif user_input == "S":
            # call show_restaurant_menu function
            pass
        elif user_input == "E":
            # call show_restaurant_menu function and exit program
            pass
        else:
            print("Invalid input. Please try again.")

def add_item_to_menu():
    name = input("Enter item name: ")
    price = input("Enter item price: ")
    item = MenuItem(name, price)
    item.save()
    print("Item was added successfully.")

def remove_item_from_menu():
    name = input("Enter item name to remove: ")
    item = MenuManager.get_by_name(name)
    if item:
        item.delete()
        print("Item was deleted successfully.")
    else:
        print("Error: Item not found.")

def update_item_from_menu():
    name = input("Enter item name to update: ")
    price = input("Enter new item price: ")
    new_name = input("Enter new item name: ")
    new_price = input("Enter new item price: ")
    item = MenuManager.get_by_name(name)
    if item:
        item.update(new_name, new_price)
        print("Item was updated successfully.")
    else:
        print("Error: Item not found.")

def show_restaurant_menu():
    items = MenuManager.all()
    for item in items:
        print(f"{item.name}: ${item.price}")