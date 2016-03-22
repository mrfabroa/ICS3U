"""
Write a trip calculator that allows the user to enter how many trips they’ve travelled (in km) and
then the distance travelled for each trip.  It should then output the total distance travelled.
"""



number_of_trips = input("How many trips did you travel?")
total_distance = 0

for i in range(1, number_of_trips + 1):
    distance = input("Enter the distance in km travelled for trip " + str(i))
    total_distance = total_distance + distance

print "The total distance travelled on your trips is", total_distance, "km."

# WHILE LOOP VERSION
number_of_trips = input("How many trips did you travel?")
total_distance = 0
count = 1

while count <= number_of_trips:
    distance = input("Enter the distance in km travelled for trip " + str(count) +": ")
    total_distance = total_distance + distance
    count += 1

print "The total distance travelled on your trips is", total_distance, "km."
