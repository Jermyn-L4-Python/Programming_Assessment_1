#Create function that takes two arguments, size and text
def make_shirt(size, text):
    print(f"The size of your shirt is {size}.")
    print(f"The text displayed on your shirt will be, '{text}'.")  

#call out the function using positional arguments
#positional argument is based on it's position in the argument list
make_shirt("small", "Make every step count")

#call out the function using keyword arguments
#keyword argument is based on the specific parameter name
make_shirt(text = "Not a morning person", size = "Large")