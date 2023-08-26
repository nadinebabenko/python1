#CREATE DATABASE mydatabase;

#CREATE TABLE Menu_Items (
 # item_id SERIAL PRIMARY KEY,
  #item_name VARCHAR(30) NOT NULL,
 # item_price SMALLINT DEFAULT 0
#);

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

import psycopg2

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        conn = psycopg2.connect(database="mydatabase", user="myuser", password="mypassword", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute("INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)", (self.name, self.price))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self):
        conn = psycopg2.connect(database="mydatabase", user="myuser", password="mypassword", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.name,))
        conn.commit()
        cur.close()
        conn.close()

    def update(self, new_name=None, new_price=None):
        conn = psycopg2.connect(database="mydatabase", user="myuser", password="mypassword", host="localhost", port="5432")
        cur = conn.cursor()
        if new_name is not None:
            cur.execute("UPDATE Menu_Items SET item_name = %s WHERE item_name = %s", (new_name, self.name))
            self.name = new_name
        if new_price is not None:
            cur.execute("UPDATE Menu_Items SET item_price = %s WHERE item_name = %s", (new_price, self.name))
            self.price = new_price
        conn.commit()
        cur.close()
        conn.close()

import psycopg2

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        conn = psycopg2.connect(database="mydatabase", user="myuser", password="mypassword", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (name,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row is not None:
            return MenuItem(row[1], row[2])
        else:
            return None

    @classmethod
    def all_items(cls):
        conn = psycopg2.connect(database="mydatabase", user="myuser", password="mypassword", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Menu_Items")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        items = []
        for row in rows:
            items.append(MenuItem(row[1], row[2]))
        return items