

def wages_earned(number_of_work_hours, hourly_rate):
    # Calculate wages
    wages = hourly_rate * number_of_work_hours
    over_40_wages = (hourly_rate * 40) + ((number_of_work_hours-40) * hourly_rate * 1.5)
    if number_of_work_hours <= 40:
        print "Your wages is", float(wages),"dollars."
    else:
        print "Your wages is",over_40_wages,"dollars"

# Get the number of work hours and the hourly rate	
number_of_work_hours = input ("Please enter the number of work hours: ")
hourly_rate = input("Please enter the hourly rate: ")

wages_earned(number_of_work_hours, hourl_rate)