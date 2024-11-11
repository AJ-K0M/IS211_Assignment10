import sqlite3

conn = sqlite3.connect('pets.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
)
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS person_pet (
    person_id INTEGER,
    pet_id INTEGER
)
''')

persons = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]

pets = [
    (1, 'Rusty', 'Dalmatian', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

person_pet = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
]

conn.executemany('INSERT INTO person VALUES (?, ?, ?, ?)', persons)
conn.executemany('INSERT INTO pet VALUES (?, ?, ?, ?, ?)', pets)
conn.executemany('INSERT INTO person_pet VALUES (?, ?)', person_pet)

conn.commit()
conn.close()

if __name__ == "__main__":
    print("Running load_pets.py")
