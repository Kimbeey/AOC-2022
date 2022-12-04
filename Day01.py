def get_max(calories):
    """
    Part 1 of Day 1
    :param calories: list that represents the Calories of the food carried the Elves
    :return: the maximal calories
    """
    max_cal = 0
    curr_cal = 0
    for i in range(0, len(calories)):
        if type(calories[i]) == str:
            if curr_cal > max_cal:
                max_cal = curr_cal
            curr_cal = 0
        else:
            curr_cal = curr_cal + calories[i]
    if curr_cal > max_cal:
        return curr_cal
    return max_cal


def get_top3(calories):
    """
    Part 2 of Day 1
    :param calories: list that represents the Calories of the food carried the Elves
    :return: the top 3 maximal calories
    """
    max1 = 0
    max2 = 0
    max3 = 0
    curr_cal = 0
    for i in range(0, len(calories)):
        if type(calories[i]) == str:
            if curr_cal > max1 and curr_cal > max2 and curr_cal > max3:
                max3 = max2
                max2 = max1
                max1 = curr_cal

            elif curr_cal > max2 and curr_cal > max3:
                max3 = max2
                max2 = curr_cal
            elif curr_cal > max3:
                max3 = curr_cal
            curr_cal = 0
        else:
            curr_cal = curr_cal + calories[i]
    if curr_cal > max1:
        max3 = max2
        max2 = max1
        max1 = curr_cal
    elif curr_cal > max2:
        max3 = max2
        max2 = curr_cal
    elif curr_cal > max3:
        max3 = curr_cal

    return max1 + max2 + max3

