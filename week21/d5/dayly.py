import requests
import random

 
response = requests.get('https://restcountries.com/v2/all')
countries = response.json()
 
random.shuffle(countries)
 
selected_countries = countries[:10]

# Extract the name, capital, flag, subregion, and population attributes for each selected country
data = []
for country in selected_countries:
    name = country['name']
    capital = country['capital']
    flag = country['flags'][0]
    subregion = country['subregion']
    population = country['population']
    data.append((name, capital, flag, subregion, population))

# Write the extracted attributes to your database
# Replace the placeholders with your database connection details and table name
import sqlite3
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()
c.executemany('INSERT INTO Menu_Items (name, capital, flag, subregion, population) VALUES (?, ?, ?, ?, ?)', data)
conn.commit()
conn.close()