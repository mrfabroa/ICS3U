__author__ = 'eric'


def count120():
    """
    prints the numbers from 100 to 120 inclusively
    :return: None
    """

    for i in range(100,121):
        print i


def start_stop(a, b):
    """
    prints the numbers between a and b inclusively
    :param a: int - start number
    :param b: int - end number
    :return: None
    """

    for i in range(a, b + 1):
        print i



def temp_table(cel1, cel2):
    """
    Prints a Celsius to Fahrenheit conversion list starting at celsius cel1 and ending at celsius cel2, printing one
    conversion every 5 degrees.
    :param cel1: int - starting temp in celsius
    :param cel2: int - ending temp in celsius
    :return: None
    """

    for c in range(cel1, cel2 + 1, 5):
        print c, "celsius =", (c * 9.0/5) + 32, "Fahrenheit"


def temp_table2(fah1, fah2):
    """
    prints a Fahrenheit to Celsius conversion list starting at fahrenheit fah1 and ending at fahrenheit fah2, printing one conversion every 5 degrees.
    :param fah1: int - starting temp in fahrenheit
    :param fah2: int - ending temp in fahrenheit
    :return: None
    """

    for f in range(fah1, fah2 + 1, 5):
        print f, "fahrenheit =", (f-32) * (5/9.0), "celsius"


def simple_interest(principal, rate):
    """
    takes in a principal and an annual interest rate, then calculates the simple
    interest earned for each year invested from 1 to 20
    :param principal: float
    :param rate: float
    :return: None
    """

    for t in range(1, 21):
        print t, "years,", "interest earned is", principal * rate * t

simple_interest(1000, 0.02)