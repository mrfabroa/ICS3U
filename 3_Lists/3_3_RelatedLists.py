__author__ = 'eric'

names = ["Iron Man", "Captain America", "Hulk", "Thor"]
phoneNumbers = ["213-536-3735", "313-374-6638" ,"212-883-8839", "402-773-8262"]

# print out the phone number for Captain America
print names[1] + ": " + phoneNumbers[1]

# print out a table of names and numbers
print "{0:20}{1:20}".format("Name","Phone Number")

for i in range(len(names)):
    print "{0:20}{1:20}".format(names[i], phoneNumbers[i])

    monthNames = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# get the month
month = raw_input("Enter the month:")

# get the day
day = input("Enter the day number in the month:")

# find the index of the month in monthNames
location = 0
while monthNames[location] != month:
    location += 1

# use the determined index to compute dayofYear

# compute the number of days prior to required month
daytotal = 0
for i in range(location):
    daytotal += daysInMonth[i]

# add the remaining days in the month to the total
daytotal += day
print daytotal
