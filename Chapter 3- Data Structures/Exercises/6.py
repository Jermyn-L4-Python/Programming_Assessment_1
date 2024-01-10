#Make a guest list for a Dinner
Guests = ["Michael Jackson", "Ryan Reynolds", "Margot Robbie", "Hugh Jackman"]

#Make a loop that prints an invitation to every person in the Guests List
for person in Guests:
    print(f"{person}, you are invited to a dinner at my place.")

#Michael Jackson cant come to dinner
print(f"\nIt seems like {Guests[0]} can't make it to dinner.")

#Replace Michael Jackson with Emily Blunt 
Guests[0] = "Emily Blunt"

#Backslash n for extra space
print("\n")

#Make another loop that prints out the newly updated List with Emily Blunt
for person in Guests:
    print(f"{person}, you are invited to a dinner at my place.")

#Ran out of space for 2 more people
print("\nOh no! We only have space for two people!")

#Remove 2 other guests by using the pop function which removes the guest from the list
name = Guests.pop()
print(f"\nI apologize {name}, we ran out of space at the table.")

name = Guests.pop()
print(f"I apologize {name}, we ran out of space at the table.")

#Make another loop to print the updated list that contains only 2 guests
for person in Guests:
    print(f"{person}, you are still invited to a dinner at my place.")

#Delete the Guests in the list to have an empty list and print out to confirm
del(Guests[0])
del(Guests[0])
print(Guests)



