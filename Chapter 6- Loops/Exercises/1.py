#As long as the prompt is true, keep on looping
while True:
    #ask user for a topping or enter a quit value
    Toppings = input("What topping would you like on your pizza? Enter 'quit' when you are finished: ")
    
    #if the user did not input a 'quit' value
    if Toppings != "quit":
        #Print this
        print(f"I am adding {Toppings} to your pizza. \n")

    #If user print a 'quit' value, stop the loop
    else:
        break