__author__ = 'eric'


def show_question(data_string):
    # split data string based on a "," separator
    data_list = data_string.split(",")

    # get first element
    question = data_list[0]

    # print first element
    print question


def check_response(user_response, data_string):
    # split data string based on a "," separator
    data_list = data_string.split(",")

    answer = data_list[-1].strip()

    if user_response == answer:
        return True
    else:
        return False

