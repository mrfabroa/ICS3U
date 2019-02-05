__author__ = 'eric'

def printN(n):
    """
    Output the numbers from 1 to n (on separate lines)
    :param n: int
    :return: None
    """

    for i in range(1, n+1):
        print i

def sum_n(n):
    """
    Return the sum of the values from 1 to n
    :param n: int
    :return: int
    """

    # initialize the accumulator
    total = 0

    # loop and build up the accumulator
    for i in range(1, n+1):
        # total = total +i
        total += i

    return total

print sum_n(5)

