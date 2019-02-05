__author__ = 'eric'


def example1():
    # initialize the total and number
    total = 0
    number = input("Enter a number: ")

    # the loop condition
    while number != -1:
        # the loop statements
        total = total + number
        number = input("Enter a number: ")

    print "The sum is", total



def example1_1():
    """
    write a program that uses a while loop to output the numbers from 1 to 10
    :return:
    """

    # for loop style
    for i in range(1,11):
        print i

    # while loop version
    count = 1 # initialize count at 1

    # repeat while count <=10
    while count <= 10:
        print count # output count
        count += 1


def example2():

    # Set the number and number of entries to be 0
    total = 0
    entries = 0

    # Read a number from the user
    number = input("Enter a number:  ")

    # while the number is not -1
    while number != -1:
        # sum = sum + number
        total = total + number

        # number of entries = number of entries + 1
        entries += 1

        # read a number from the user
        number = input("Enter a number:  ")

    # Output sum/number of entries
    print float(total)/entries



def largest():
    biggest = 0
    number = input("Enter number here: ")

    while number != -1:
        if number > biggest:
            biggest = number
        number = input("Enter number here: ")
    print biggest


def infinite():
    # repeat while count <=10
    count = 1
    while count <= 10:
        print count # output count
        #count += 1 --> commenting this out causes an infinite loop





