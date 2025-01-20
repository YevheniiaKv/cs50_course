people = [
    {"name": "Harry", "house": "Griffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
def f(person):
    return person["name"]
    
people.sort(key=f)

print(people)

# scenario 2
people = [
    {"name": "Harry", "house": "Griffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
def f(person):
    return person["house"]
    
people.sort(key=f)

print(people)

# scenario 3, де ми використовуємо lambda функцію у функції sort, щоб спростити вираз:

people = [
    {"name": "Harry", "house": "Griffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

    
people.sort(key=lambda person: person["name"])

print(people)