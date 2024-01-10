while True:
    #Ask for age input
    Age = int(input("What is your age? "))
    # If age is less than 3
    if Age < 3:
        print("Your ticket is free!")
    #If age is less than or equal to 12
    elif Age <= 12:
        print("Your ticket is $10.")
    #If none of the above
    else: 
        print("Your ticket is $15.")
