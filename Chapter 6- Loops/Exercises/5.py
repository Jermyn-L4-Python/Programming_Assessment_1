#List with added three Pastrami
sandwich_orders = ["Chicken Sandwich", "Pastrami", "Ham Sandwich", "Pastrami", "Nutella Sandwich", "Pastrami" ,"Steak Sandwich"]

#Empty List
finished_sandwiches = []

print("The deli has ran out of Pastrami.")
#For every pastrami in sandwich orders
while "Pastrami" in sandwich_orders:
    #delete pastrami using .remove()
    sandwich_orders.remove("Pastrami")


while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I am making your {sandwich}.")
    finished_sandwiches.append(sandwich)
    
print("\n")

for sandwich in finished_sandwiches:
    print(f"I made your {sandwich}.")