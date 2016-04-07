__author__ = 'eric'

def problem1():
    biggest = 0
    number = input("Enter number here: ")

    while number != -1:
        if number > biggest:
            biggest = number
        number = input("Enter number here: ")
    print biggest


def problem_2():
    """
    Write a program that lets you continuously enter a word and it prints out the number of vowels
    and the number of consonants (vowels are: a,e,i,o,u. all others are consonants) until the word 'stop' is entered.

    :return:None
    """

    #initialize the word
    word = raw_input("Enter a word: ")



    # repeat until the word 'stop is entered'
    while word != 'stop':
        consonant_count = 0
        vowel_count = 0

        #count the vowels and consonants in the word
        for letter in word:
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y':
                vowel_count += 1
            else:
                consonant_count +=1

        print "vowels --> ", vowel_count
        print "consonants -->",consonant_count

        #get another word
        word = raw_input("Enter a word: ")


def problem3():
    """
    Write a program that prompts the user for a school supplies budget value in dollars.
    It will then ask the user to enter the name, unit price and quantity of an item and output
    the remaining budget dollars until they've spent more than their set budget.

    :return: None
    """

    budget = input("Enter the school supplies budget: ")

    while budget >= 0:
        print ""
        item = raw_input("Enter an item to buy: ")
        unit_price = input("Enter the unit price of the item: ")
        quantity = input("Enter the quantity: ")
        budget = budget - (unit_price * quantity)
        print ""
        print "You have", round(budget, 2) , "remaining in your budget."


def div2(num):
    """
    Write a function div2(num), that uses a loop to compute and return how many times
    num can be divided by 2.  Assume n > 0.
    :param num: int
    :return: int
    """

    count = 0
    while num > 0:

        if num > 0:
            num = num - 2
            count +=1

    return count

def kthDigit(n, k):
    """
    Write the function kthDigit(n, k):  this returns the kth digit in the integer n.
    returns -1 if k >= # of digits in n.
    :param n:
    :param k:
    :return:
    """

    # convert n to a string
    n_string = str(n)
    digit_str = ""

    for i in range(k):
        digit_str = n_string[i]

    return digit_str


