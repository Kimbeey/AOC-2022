import re


def get_list(my_file):
    """
       get a list for Day 1
       :param my_file: the strings to convert into a list
       :return: a list
    """
    L = []
    for line in my_file.readlines():
        my_var = line.strip()
        if my_var:
            my_var = int(my_var)
        L += [my_var]
    return L


def get_lists(my_file):
    """
    get a list for Day 2 and 3
    :param my_file: the strings to convert into a list
    :return: a list
    """
    L = []
    for line in my_file.readlines():
        my_var = line.strip()
        L += [my_var]
    return L


def get_lis(my_file):
    """
    get a list for Day 4
    :param my_file: the strings to convert into a list
    :return: a list
    """
    L = []
    for line in my_file.readlines():
        my_var = line.strip()
        L += [my_var]

    LL = []
    for nums in L:
        x = nums.split(',')
        LL += x
    return LL


def lists_for_moves(my_file):
    """
    get a list for day 5
    :param my_file:
    :return:
    """
    stop = False
    cargo = []
    L = []
    for line in my_file.readlines():
        if line[0] != '\n' and line[1].isdigit():
            stop = True
        elif stop and line[0] == 'm':
            direction = []
            moves = line.strip().split(' ')
            for i in range(0, len(moves)):
                if moves[i].isdigit():
                    direction += [int(moves[i])]
            L += [direction]
        else:
            my_list = [line[idx:idx + 4].strip() for idx in range(0, len(line), 4)]
            cargo += [my_list]
    return cargo, L


