#Assign budget and cost per piece to variable
budget = 50
cost = 6

#Make formula to get the quantity and pounds remaining
amount = int(budget / cost) 

pounds_left = budget - amount * cost

#Output answer
print(f"USB sticks she can buy: {amount}")

print(f"Pounds she has left: {pounds_left}")