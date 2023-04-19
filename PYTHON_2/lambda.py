people = [
    {"name": "Sean", "house": "Tawan"},
    {"name": "Dylan", "house": "Kajewa"},
    {"name": "John", "house": "Kajewa"},
    {"name": "Rama", "house": "Midtown"}
]
# people[3]["house"] = "Zinga"
# def f(person):
#    return person["house"]
# people.sort(key=f)

people.sort(key=lambda person:person["house"])

print(people)