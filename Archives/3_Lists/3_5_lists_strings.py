
def immutable_demo():
    myString = 'hello'
    print myString[0]

    myString[0] = 'j'

def mutable_demo():
    myList = ['h', 'e', 'l',' l', 'o']
    print myList[0]
    myList[0] = 'j'
    print myList

def captilalize_demo():
    s = "simulation"
    cap = s.capitalize()
    print s
    print cap

def strip_demo():
    word = "   \t\nhello    \n"
    print "*" + word + "*"
    print "*" + word.strip() + "*"


def search_demo():
    word = "something"
    location = word.find("x")
    print location

def count_demo():
    word = "Apple"
    count = word.count("p")
    print count

def count_list_demo():
    mylist = [1,2,3,4,5,6,4,7,4,8]

    print mylist.count(4)
    print mylist.index(4)

def split_demo():
    sentence = "She sells sea shells down by the sea shore"
    word_list = sentence.split(" ")
    print word_list

    mydate = "04/14/2016"
    date_list = mydate.split("/")
    print date_list

def join_demo():
    mylist = ["h", "e", "l", "l", "o"]
    mystring = "".join(mylist)
    print mystring

join_demo()


