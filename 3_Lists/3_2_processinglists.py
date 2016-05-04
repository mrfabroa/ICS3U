__author__ = 'eric'

def append_command():
    my_list = [2,4,5,6]
    print my_list
    my_list.append(9)
    print my_list


def user_append():
    my_list = [] # Empty list

    for i in range(5):
        userInput = input( "Enter an integer: ")
        my_list.append(userInput)
        print(my_list)

def zero_list():
    my_list = [0] * 10
    print my_list

def list_sum1():
    # Copy of the array to sum
    myArray = [5,76,8,5,3,3,56,5,23]

    # Initial sum should be zero
    list_sum = 0


    # Loop from 0 up to the number of elements
    # in the array:
    for i in range(len(myArray)):
        # Add element 0, next 1, then 2, etc.
        list_sum = list_sum + myArray[i]

    # Print the result
    print list_sum


def list_sum2():
    # Copy of the array to sum
    myArray = [5,76,8,5,3,3,56,5,23]

    # Initial sum should be zero
    list_sum = 0


    # Loop from 0 up to the number of elements
    # in the array:
    for i in myArray:
        # Add element 0, next 1, then 2, etc.
        list_sum = list_sum + i

    # Print the result
    print list_sum


def double():
    # Copy of the array to modify
    myArray = [5,76,8,5,3,3,56,5,23]

    # Loop from 0 up to the number of elements
    # in the array:
    for i in range( len(myArray) ):
        # Modify the element by doubling it
        myArray[i] = myArray[i] * 2

    # Print the result
    print( myArray )

def double2():
    # Copy of the array to modify
    myArray = [5,76,8,5,3,3,56,5,23]

    # Loop from 0 up to the number of elements
    # in the array:
    for item in myArray:
        # Modify the element by doubling it
        item = item * 2

    # Print the result
    print( myArray )


double2()