#Exercise 1 : Family
class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations on the new addition to the family! {kwargs['name']} was born.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"The {self.last_name} family members are:")
        for member in self.members:
            print(member['name'])

#Exercise 2 : TheIncredibles Family

class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                print(f"{member['incredible_name']} used their {member['power']} power!")
                return
        print(f"{name} is not a member of the Incredibles family.")

    def family_presentation(self):
        print(f"The {self.last_name} family members are:")
        for member in self.members:
            print(f"{member['incredible_name']} ({member['name']})")

class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['incredible_name']} used their {member['power']} power!")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old.")
                return
        print(f"{name} is not a member of the Incredibles family.")

    def incredible_presentation(self):
        super().family_presentation()
        print("The Incredibles' powers are:")
        for member in self.members:
            print(f"{member['incredible_name']} ({member['name']}): {member['power']}")

# Adding Baby Jack
the_incredibles = TheIncredibles("Parr", [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
])
the_incredibles.born(name='Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='Baby Jack')

# Presenting the Incredibles
the_incredibles.incredible_presentation()