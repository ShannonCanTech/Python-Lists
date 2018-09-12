# Prints the first 2 items in list
guests = ['Martha Stewart', 'Snoop Dog', 'Michael Jackson', 'Whitney Houston', 'Aretha Franklin']
for guest in guests[0:2]:
    print "Hi " + guest + ". You are uninvited."

# Deletes first 2 items in list
del guests[0:2]
# Prints the remaining guests in list
for guest in guests:
    print "Hi " + guest + "! You are confirmed to attend the event."

# Adds guests to end of list
guests.append('Ariana Grande')
guests.append('Beyonce')
# Prints the added guests in list
for guest in guests[3:]:
    print "Hello " + guest + "! You are officially invited."