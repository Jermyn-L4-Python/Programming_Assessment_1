#Make list of places I want to visit
Places = ["Maldives", "Amsterdam", "Japan", "Korea", "Iceland"]

#Print the List
print("Original: ")
print(Places,"\n")

#Print the list using "sorted()" to make it alphabetical
print("Alphabetical: ")
print(sorted(Places),"\n")

#Print the original list to show that no changes are made with the List
print("Original: ")
print(Places, "\n")

#Print the list using "sorted()" and "reverse = true" to make it reversed alphabetica;
print("Reverse Alphabetical: ")
print(sorted(Places, reverse = True), "\n")

#Print the original list to show that no changes are made with the List
print("Original: ")
print(Places, "\n")

#Print the list using the function .reverse() to reverse the original list
print("Reversed: ")
Places.reverse()
print(Places, "\n")

#Print again with .reverse to bring it back to original order
print("Original: ")
Places.reverse()
print(Places, "\n")

#Use sort to replace the original list into alphabetical order
print("Alphabetical: ")
Places.sort()
print(Places, "\n")

#Use sort to replace the original list into reverse alphabetical order
print("Reverse Alphabetical: ")
Places.sort(reverse = True)
print(Places)