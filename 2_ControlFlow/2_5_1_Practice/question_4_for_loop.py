"""
Modify #4 so that it calculates the total amount spent on fuel by allowing the user to specify the fuel economy of a car (litres/100 km),
and then output the distance and cost of fuel (in $/L) for the total trip
"""

fuel_economy = input("Enter the fuel economy of your car (L/100km): ")
cost_of_fuel = input("Enter the cost of fuel (for one litre): ")

number_of_trips = input("How many trips did you travel?")
total_distance = 0
fuel_total = 0

for i in range(1, number_of_trips + 1):
    distance = input("Enter the distance in km travelled for trip " + str(i) + ": ")
    total_distance = total_distance + distance
    fuel_total = fuel_total + ((distance / 100.0) * fuel_economy * cost_of_fuel)


print "The total distance travelled on your trips is", total_distance, "km."
print "The total fuel cost is $"+str(fuel_total)

