__author__ = 'eric'
import random

def change_counter():

    print "Change Counter"
    print ""
    print "Please enter the count of each coin type."
    quarters = input("Quarters: ")
    dimes = input("Dimes: ")
    nickels = input("Nickels: ")
    pennies = input("Pennies: ")
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print ""
    print "The total value of your change is ${0:0.2f}".format(total)

def print_receipt():
    cost1 = 3.06
    tax1 = cost1 * 0.06
    total1 = cost1 + tax1

    print "Cost:  ${0:5.2f}".format(cost1)
    print "Tax:    {0:5.2f}".format(tax1)
    print "------------"
    print "Total: ${0:5.2f}".format(total1)

def demo_table():

    # Header
    print "{0:>3} {1:>6}{2:>15}".format("#","Score", "Name")
    print "-"*30

    for i in range(101):
        print "{0:3} {1:6}{2:>15}".format(i, random.randint(0, 1000),"Garvin Doyle")

def fuel_efficency():
    litres_max = 70
    fuel_efficiency = 13.9 #L/100km

    #table header
    print "{0:>16} {01:>22}".format("Litres Used","Distance Travelled")

    for litres in range(0,litres_max,10):
        distance = (100*litres)/fuel_efficiency
        print "{0:15}L {01:20.2f}km".format(litres,distance)

fuel_efficency()