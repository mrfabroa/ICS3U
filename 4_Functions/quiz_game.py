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

    if user_response.lower() == answer.lower():
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
    Asks questions and updates score accordingly
    :param datafile: file object - a file object created via an open() call
    :return: int - the final score of the player
    """
    pass

    # COMPLETE THIS FUNCTION
    # initialize score
    # repeat
        # read a line from data file
        # show question
        # show options
        # get user response
        # check response (use check response function)
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
    """
    A quiz game.  Data is read from a source text file.
    :return:
    """
    myfile = open_datafile("quiz_data.txt")
    final_score = process_questions(myfile)
    show_final_score(final_score)

main()