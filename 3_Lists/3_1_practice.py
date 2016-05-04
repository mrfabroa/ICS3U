__author__ = 'eric'


def middleway(list_a, list_b):
    """
    Given 2 int lists, list_a and list_b, each length 3,
    write a function middle_way(list_a,list_b) that returns
    a new list length 2 containing their middle elements.
    :param list_a: int[]
    :param list_b: int[]
    :return: int[]
    """

    list_c = [list_a[1], list_b[1]]

    return list_c


def common_end(list_a, list_b):
    """
    Given 2 lists of ints, list_a and list_b,
    write a function common_end(list_a, list_b) and
    return True if they have the same first element
    or they have the same last element.
    Both lists will be length 1 or more.
    :param list_a: int[]
    :param list_b: int[]
    :return: Boolean
    """

    if (list_a[0] == list_b[0]) or (list_a[-1] == list_b[-1]):
        return True
    else:
        return False


def max_end3(list3):
    """
    given a list (list3) of ints length 3, figure out which is
    larger between the first and last elements in the list,
    set all the other elements to be that value. Return the changed list.
    :param list3: int
    :return: int[]
    """

    # compare first and last elements
    if list3[0] > list3[2]:
        list3[1] = list3[0]
        list3[2] = list3[0]

    elif list3[0] < list3[2]:
        list3[0] = list3[2]
        list3[1] = list3[2]

    return list3
