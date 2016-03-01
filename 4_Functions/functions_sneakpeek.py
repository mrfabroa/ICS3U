__author__ = 'eric'

def my_sqrt(x):
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
    if (a_smile and b_smile) or (not(a_smile) and not(b_smile)):
        return True
    else:
        return False

def monkey_trouble2(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False


def near_hundred(n):
    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    else:
        return False

def near_hundred_abs(n):
    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    else:
        return False

print near_hundred(80)
print near_hundred(95)
print near_hundred(115)
print near_hundred(110)

print near_hundred(180)
print near_hundred(195)
print near_hundred(215)
print near_hundred(210)
