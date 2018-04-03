import sqlite3

def create_table():
    conn = sqlite3.connect('lite.db')  # creates the db file if does not exist yet
    cursor = conn.cursor()
    query_create = "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)"
    cursor.execute(query_create)
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    conn = sqlite3.connect('lite.db')  # creates the db file if does not exist yet
    cursor = conn.cursor()
    query_insert_data = "INSERT INTO store VALUES (?, ?, ?)"
    cursor.execute(query_insert_data, (item, quantity, price))
    conn.commit()
    conn.close()

def view_data():
    conn = sqlite3.connect('lite.db')  # creates the db file if does not exist yet
    cursor = conn.cursor()
    query_view_data = "SELECT * FROM store"
    cursor.execute(query_view_data)
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_data(item):
    conn = sqlite3.connect('lite.db')  # creates the db file if does not exist yet
    cursor = conn.cursor()
    query_delete_data = "DELETE FROM store WHERE item = ?"
    cursor.execute(query_delete_data, (item,))
    conn.commit()
    conn.close()

def update_data(item, quantity, price):
    conn = sqlite3.connect('lite.db')  # creates the db file if does not exist yet
    cursor = conn.cursor()
    query_update_data = "UPDATE store set quantity = ?, price = ? WHERE item = ?"
    cursor.execute(query_update_data, (quantity, price, item))
    conn.commit()
    conn.close()

#insert_data('Coffee Cup', 10, 2.3)
print(view_data())
#delete_data('Coffee Cup')
update_data('Wine Glass', 25, 8.75)
print(view_data())