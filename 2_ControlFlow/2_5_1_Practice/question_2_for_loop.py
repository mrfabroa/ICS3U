

"""
Write a cash register program that allows the user to enter the price AND quantity for each product they want to purchase.
Output the total cost with 13% tax applied
"""


number_of_items = input("How many items do you want to buy: ")
price = 0
quantity = 0
total_cost = 0

for i in range(1, number_of_items + 1):
    price = input("Enter the price of product " + str(i) + ": ") 
    quantity = input("Enter the quantity of product " + str(i) + ": ")
    cost = price * quantity
    total_cost = total_cost + cost

# apply tax to the total cost
total_cost  = total_cost + (total_cost * 0.13)
print "The total with tax is $", total_cost
