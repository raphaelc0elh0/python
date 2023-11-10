import os
import sqlite3

dir_path = os.path.dirname(os.path.realpath(__file__))
conn = sqlite3.connect(f"{dir_path}/friends.db")

c = conn.cursor()

#
# creating table
#

c.execute("""
  CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER)
""")

#
# inserting
#

first_name = "Raphael"
last_name = "Coelho"
closeness = 7
c.execute("""
  INSERT INTO friends
  (first_name, last_name, closeness)
  VALUES (?, ?, ?)
""", (first_name, last_name, closeness))

#
# inserting bulk
#

people = [
    ("Raphael", "Pinheiro", 30),
    ("John", "Doe", 25),
    ("Alice", "Johnson", 30),
    ("Bob", "Smith", 22),
    ("Emily", "Williams", 28),
    ("Charlie", "Brown", 35)
]

c.executemany("""
  INSERT INTO friends
  VALUES (?, ?, ?)
""", people)

#
# selecting
#

c.execute("""
  SELECT *
  FROM friends
  WHERE first_name IS 'Raphael'
""")
print(c.fetchone())
print(c.fetchall())

conn.commit()
conn.close()
