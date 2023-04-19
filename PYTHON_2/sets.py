# create an empty set
s = set()

# add element
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

s.remove(3)
print(s)

print(f"The set has {len(s)} elements.")