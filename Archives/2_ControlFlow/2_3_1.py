__author__ = 'eric'
"""
Many companies pay time-and-a-half for any hours worked above 40 in a given week.
Write a program to input the number of
hours worked and the hourly rate and calculate the total wages for the week.
"""

# get inputs - hours, payrate
hours = input("Please enter the hours worked: ")
payrate = input("Please enter your pay rate:  ")

# compute total wages
if hours > 40:
    total_wages = 40*payrate + (hours - 40)*(1.5*payrate)
else:
    total_wages = hours*payrate

# output total wages
print "The total wages earned this week is", total_wages