__author__ = 'eric'

def my_sqrt(x):
    """
    Compute the square root of x
    :param x: int - non-negative value to square root
    :return: float
    """
    square_root = x**(0.5)
    return square_root


def sum_double(a, b):
    """
    Write a function sum_double(a, b),
    given two int values, return their sum.
    Unless the two values are the same,
    then return double their sum.
    :param a: int
    :param b: int
    :return: int
    """
    if a == b:
        return 2*(a+b)
    else:
        return a+b

def monkey_trouble(a_smile, b_smile):
    """
    Write a function monkey_trouble(a_smile,b_smile), where we have two monkeys,
    a and b, and the parameters a_smile and b_smile indicate if each is smiling.
    We are in trouble if they are both smiling or if neither of them is smiling.
    Return True if we are in trouble.
    :param a_smile: bool - monkey 1 - True if smiling
    :param b_smile: bool - monkey 2 - True if smiling
    :return: bool
    """
    if (a_smile and b_smile) or (not(a_smile) and not(b_smile)):
        return True
    else:
        return False

def monkey_trouble2(a_smile, b_smile):
    """
    Write a function monkey_trouble(a_smile,b_smile), where we have two monkeys,
    a and b, and the parameters a_smile and b_smile indicate if each is smiling.
    We are in trouble if they are both smiling or if neither of them is smiling.
    Return True if we are in trouble.
    :param a_smile: bool - monkey 1 - True if smiling
    :param b_smile: bool - monkey 2 - True if smiling
    :return: bool
    """
    if a_smile == b_smile:
        return True
    else:
        return False


def near_hundred(n):
    """
    When given an int n, return True if it is within 10 of 100 or 200.
    :param n: an integer
    :return: bool
    """
    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    else:
        return False

def near_hundred_abs(n):
    """
    When given an int n, return True if it is within 10 of 100 or 200. Uses abs() function
    :param n: an integer
    :return: bool
    """
    if abs(100-n) <= 10 or abs(200-n):
        return True
    else:
        return False

def to_fahrenheit(celsius):
    """
    Convert a given celsius to fahrenheit
    :param celsius: float - temp in celsius to convert
    :return: float - the resulting temp in fahrenheit
    """

    return (1.8*celsius) + 32
