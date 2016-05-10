__author__ = 'eric'


def example1():
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

def example1_1():
    """
    Demo of readline - read the first 5 names of a text file and output them to the screen.  Adjusted to clean up extra trailing whitespace
    :return: None
    """

    namesfile = open("names.txt")

    for i in range(5):
        # read a line from a file, remove extraneous white space
        name = namesfile.readline().strip()
        print name

    namesfile.close



def example2():
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


def example3():
    """
    Demo of readlines().  Read all names from a text file into a list.  print the first and last names in the list
    :return: none
    """

    namesfile = open('names.txt','r')
    nameslist = namesfile.readlines()

    print nameslist[0].strip()
    print nameslist[len(nameslist)-1].strip()

example3()





