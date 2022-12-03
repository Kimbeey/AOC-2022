def get_list(my_file):
    L = []
    for line in my_file.readlines():
        my_var = line.strip()
        if my_var:
            my_var = int(my_var)
        L += [my_var]
    return L


def get_lists(my_file):
    L = []
    for line in my_file.readlines():
        my_var = line.strip()
        L += [my_var]
    return L