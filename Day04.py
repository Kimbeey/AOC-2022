
def get_overlap(pairs):
    """
    Part 1 of Day 4
    :param pairs: the list of the section assignments for each pair
    :return: how many pairs overlap completely
    """
    overlaps = 0
    for i in range(0, len(pairs), 2):
        # get the ids of the elves
        sec11, sec12 = pairs[i].split('-')
        sec21, sec22 = pairs[i + 1].split('-')
        if (int(sec11) >= int(sec21) and int(sec12) <= int(sec22)) or (
                int(sec21) >= int(sec11) and int(sec22) <= int(sec12)):
            overlaps += 1
    return overlaps


def get_total_overlaps(pairs):
    """
    Part 2 of Day 4
    :param pairs: the list of the section assignments for each pair
    :return: how many pairs overlap partially
    """
    overlaps = 0
    for i in range(0, len(pairs), 2):
        # get the ids of the elves
        sec11, sec12 = pairs[i].split('-')
        sec21, sec22 = pairs[i + 1].split('-')
        if (int(sec21) <= int(sec11) <= int(sec22)) or (
                int(sec11) <= int(sec21) <= int(sec12)):
            overlaps += 1
    return overlaps
