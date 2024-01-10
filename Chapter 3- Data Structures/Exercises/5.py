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