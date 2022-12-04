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