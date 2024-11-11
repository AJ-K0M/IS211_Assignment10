import sqlite3

def person_pets(person_id):

    conn = sqlite3.connect('pets.db')

   
    person = conn.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,)).fetchone()
    
    if person:
        print(f"{person[0]} {person[1]}, {person[2]} years old")
        
        pets = conn.execute('''
        SELECT pet.name, pet.breed, pet.age, pet.dead
        FROM pet
        JOIN person_pet ON pet.id = person_pet.pet_id
        WHERE person_pet.person_id = ?
        ''', (person_id,)).fetchall()
        
        for pet in pets:
            status = "that was" if pet[3] else "that is"
            print(f"  - {person[0]} owned {pet[0]}, a {pet[1]} {status} {pet[2]} years old.")
    else:
        print("Person not found.")

    conn.close()

if __name__ == "__main__":
    print("Running query_pets.py")
    
    while True:
        try:
            person_id = int(input("Enter person ID (or -1 to exit): "))
            if person_id == -1:
                break
            person_pets(person_id)
        except ValueError:
            print("Please enter a valid ID.")
