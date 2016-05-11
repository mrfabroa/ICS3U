__author__ = 'eric'


def example1_1():
    """
    Demo readline().  Read the first two names from a text file names.txt and print them out
    :return: None
    """

    namesfile = open("names.txt", 'r')

    name1 = namesfile.readline()
    name2 = namesfile.readline()

    print name1
    print name2

    namesfile.close()


def example1_2():
    """
    Demo of readline - read the first 5 names of a text file and output them to the screen
    :return: None
    """

    namesfile = open("names.txt")

    for i in range(5):
        # read a line from a file
        name = namesfile.readline()
        print name

    namesfile.close()


def example1_3():
    """
    Demo of readline - read the first 5 names of a text file and output them to the screen.  Adjusted to clean up extra trailing whitespace
    :return: None
    """

    namesfile = open("names.txt")

    for i in range(5):
        # read a line from a file, remove extraneous white space
        name = namesfile.readline().strip()
        print name

    namesfile.close()


def practice1():
    """
    Prints out the longest name in the first 10 names in names.txt
    :return:
    """
    pass #replace with your code


def example1_4():
    """
    Demo of readline - working with integers.  Compute the average of the first 5 marks in a text file of integers (one mark per line)

    :return: float - average of the first 5 marks
    """

    # open the file in read mode
    marksfile = open("marks.txt", 'r')

    total = 0
    for i in range(5):
        # read a single mark from the file, convert it to integer
        mark = int(marksfile.readline())
        total += mark

    print total/5.0

    marksfile.close()


def example2_1():
    """
    Demo of readlines().  Read all names from a text file into a list.  print the first and last names in the list
    :return: none
    """

    namesfile = open('names.txt','r')
    nameslist = namesfile.readlines()

    print nameslist[0].strip()
    print nameslist[len(nameslist)-1].strip()

    namesfile.close()


def example2_2():
    """
    Demo of readlines().  Print out the highest mark in the class
    :return: None
    """

    marksfile = open('marks.txt', 'r')

    # read the contents of the text file into a list
    markslist = marksfile.readlines()

    highest = 0

    for i in range(len(markslist)):
        value = int(markslist[i])
        if value > highest:
            highest = value

    print highest

    marksfile.close()


def practice2():
    """
    Write a program that uses readlines() prints the average of the last 10 marks in marks.txt
    :return:
    """
    pass #replace with your code


def example3():
    """
    demo of read().
    :return:

    """

    # read in the first byte(character) of the file
    namesfile = open('names.txt', 'r')
    firstread = namesfile.read(1)
    print firstread

    # read in a single byte from current position
    secondread = namesfile.read(1)
    print secondread

    # read in three bytes from current position
    thirdread = namesfile.read(3)
    print thirdread







