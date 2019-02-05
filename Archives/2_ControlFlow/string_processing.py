__author__ = 'eric'

def combine(word1, word2):
    """
    returns a string of word1 and word2 combined together.

    :param word1: str
    :param word2: str
    :return: str
    """
    return word1 + word2


def date_abbrev(month_Num):
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"


def pwdlen(password_str):
    """
    returns True if the password_str length is longer than 6.

    :param password_str: str
    :return: bool
    """

    if len(password_str) > 6:
        return True
    else:
        return False

def username_gen(first_name, last_name):
    """
    computes a corresponding username where username is the first name first initial
    + first 7 characters of the last name

    i.e John Anderson --> JAnderso

    :param first_name: str
    :param last_name: str
    :return: str
    """
    return first_name[0] + last_name[:7]

print username_gen('Maxwell','Fabroa')

word = "hello"
for ch in word:
    print ch