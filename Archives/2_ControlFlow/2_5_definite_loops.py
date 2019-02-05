__author__ = 'eric'


def hello5():
    """
    Say hello 5 times
    :return: None
    """

    for i in range(5):
        print "hello"


def count4():
    """
    Count to 4
    :return: None
    """

    for i in range(5):
        print i


def count_5to9():
    """
    Count 5 to 9
    :return: None
    """

    for i in range(5,10):
        print i


def even_jump():
    """
    Count evenly to 18
    :return: None
    """

    for i in range(0, 20, 2):
        print i

def count_back():
    """
    Countdown from 20 to 1
    :return:
    """

    for i in range(20, 0, -1):
        print i

count_back()