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


def terminal(code):
    dir_of_dir = {}
    size = {}
    get_info = False
    current_dir = -1
    for line in code.readlines():
        words = line.strip().split(" ")
        if line.startswith("$ cd"):
            if words[-1] == "/":
                current_dir = "/"
            elif words[-1] == "..":
                all_dirs = list(dir_of_dir.keys())
                current_dir = all_dirs[all_dirs.index(current_dir) - 1]
            else:
                current_dir = words[-1]
        if line.strip() == "$ ls":
            if current_dir not in dir_of_dir:
                dir_of_dir[current_dir] = []
            get_info = True
        elif line.startswith("$"):
            get_info = False
        if get_info and line.startswith("dir"):

            dir_of_dir[current_dir] += [words[-1]]

        if line[0].isdigit():
            if current_dir not in size:
                size[current_dir] = 0
            size[current_dir] += int(line.split(" ")[0])

    return size, dir_of_dir


def list_of_list(trees):
    all_heights = []
    for line in trees:
        line = line.strip()
        heights = [int(char) for char in line]
        all_heights += [heights]
    return all_heights
