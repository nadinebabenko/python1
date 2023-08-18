class PlayerCharacter:
    # Class Object Attribute
    membership = True # static attribute    

    def __init__(self, name, age):
        if (self.membership):
            self.name = name
            self.age = age 
    def shout(self):
        print(f'My name is {self.name}')
        return 'done'
         

player1 = PlayerCharacter('Nadya', 29)
player2 = PlayerCharacter('Dima', 33)
 
print(player1.shout())
print(player2.shout())

 