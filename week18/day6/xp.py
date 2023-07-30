#Exercise 1 : Convert Lists Into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = dict(zip(keys, values))
print(my_dict)

#Exercise 2 : Cinemax #2
#1
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")

#2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

familage= list(family.values())

rickprice=15
bethprice=10
mortyprice=5
summerprice=rickprice+bethprice+mortyprice

print("The total family price is:" + str(summerprice))

#3 Zara


brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 2,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": "pink, green"        
    },
    "country_creation" : "Spain" 
}
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
else:
    brand["international_competitors"] = ["Desigual"]


brand.pop("creation_date", None)
last_international_competitor = brand["international_competitors"][-1]  
print(last_international_competitor)
us_major_colors = brand["major_color"]["US"]
print(us_major_colors)
num_key_value_pairs = len(brand)
print(num_key_value_pairs)

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

number_of_stores = brand["number_stores"]
print(number_of_stores)

#Exercise 4 : Disney Characters


users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
for index, user in enumerate(users, 1):
    print(f"User {index}: {user}")

    sorted_users = sorted(users)
for index, user in enumerate(sorted_users, 1):
    print(f"User {index}: {user}")
