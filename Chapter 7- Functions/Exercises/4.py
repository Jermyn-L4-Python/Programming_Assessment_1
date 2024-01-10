#Create a similar function as exercise 3 but with a fixed argument 
def make_shirt(size = "Large", text = "I love Python!"):
    print(f"The size of your shirt is {size}.")
    print(f"The text displayed on your shirt will be, '{text}'.")  

#Print out the original arguments
make_shirt()

#Replace the size argument with "Medium"
make_shirt(size = "Medium")

#Replace both arguments with a new value
make_shirt(size = "small", text = "Good vibes only")