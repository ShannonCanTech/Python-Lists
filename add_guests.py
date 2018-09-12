# Print pre-defined guest list
guests = ['Martha Stewart', 'Snoop Dog', 'Michael Jackson', 'Whitney Houston', 'Aretha Franklin']
print guests

# Adds guests to beginning of list
guests.insert(0, 'Janet Jackson')
print guests

# Gets length of list, divides it in half, and adds guests to the middle of list
numOfGuests = guests.__len__()
numOfGuests /= 2
guests.insert(numOfGuests, 'Britney Spears')
print guests

# Appends guest to the end of list
guests.append('Sam Smith')
print guests