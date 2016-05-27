__author__ = 'eric'




def show_question(data_string):
    """
    Extracts a question from the data_string and displays it on the screen
    :param data_string:  string - line of data from text file
    :return:
    """
    # split data string based on a "," separator
    data_list = data_string.split(",")

    # get first element
    question = data_list[0]

    # print first element
    print question


def check_response(user_response, data_string):
    """
    Compares the user response to the correct answer

    :param user_response: string - answer provided by the user
    :param data_string: string - line of data from text file
    :return: boolean - True is user response is correct
    """
    # split data string based on a "," separator
    data_list = data_string.split(",")

    # get the last value from the
    answer = data_list[-1].strip()

    if user_response == answer:
        return True
    else:
        return False


def open_datafile(filename):
    """
    open a the data file
    :param filename: string - name of file to open
    :return:file object
    """
    return open(filename, 'r')


def show_options(data_string):
    """
    Extracts the 3 options for a question from the data_string and displays them on the screen
    :param data_string:
    :return: None
    """

    # COMPLETE THIS FUNCTION
    pass



def process_questions(datafile):
    """

    :param datafile:
    :return:
    """

    # COMPLETE THIS FUNCTION
    # initialize score
    # repeat
        # read question from data file
        # show question
        # show options
        # get user response
        # check response
        # update score
    # return score

def show_final_score(final_score):
    """
    Shows the final score on the screen in an exciting way
    :param final_score: int - the final user score
    :return: None
    """

    pass


def main():
    myfile = open_datafile("quiz_data.txt")
    final_score = process_questions(myfile)
    pass