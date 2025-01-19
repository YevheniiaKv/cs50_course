# set - collection of unique values - множина - колекція унікальних значень (кожне зустрічається лише раз), порядок не важливий.

# Create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

print(s)

s.add(3)
print(s)

s.remove(2)
print(s)

len(s)
print("The set has", len(s), "numbers")

len(s)
print(f"The set includes {len(s)} elements.")
