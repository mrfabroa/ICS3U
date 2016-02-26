__author__ = 'eric'
"""
The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph over the limit plus a penalty of $200
for any speed over 90 mph. With the speed limit of 80 mph, write a program that accepts a clocked speed and either
prints a message indicating the speed was legal or prints the amount of the fine, if the speed is illegal
"""

# get speed
speed = input("Enter the speed:  ")
speed_limit = 80

# calculate fine
if speed <= speed_limit:
    fine = 0

elif speed > speed_limit:
    fine = 50 + (speed - speed_limit)*5

    if speed > 90:
        fine = fine + 200

# output fine
if fine == 0:
    print "No fine"
else:
    print "The fine is", fine