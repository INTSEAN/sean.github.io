"""class Point():
    def __init__(self, xcoordinates, ycoordinates):
        self.z = xcoordinates
        self.y = ycoordinates

p = Point(9, 20)
print(p.z)
print(p.y)
"""
class Flight():
    def __init__(self, capacity):
        self.c = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.c - len(self.passengers)

flight = Flight(4)
people = ["Harry", "Rade", "Gefred", "Frats", "Georgia"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"{person} was added to flight!")
    else:
        print(f"No available seats for {person}!")