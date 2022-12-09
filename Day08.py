def get_visible(heights):
    """
    Get the number of visible trees -> part 1 of day 8
    :param heights: all the heights of trees in a multi-dimensional list
    :return: the number of visible trees
    """
    columns = len(heights[0])
    rows = len(heights)
    visible = 2 * columns + 2 * rows - 4
    # iterate over the trees in the middle
    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            # see if the tree is the shortest in its row and column
            if shortest(heights, i, j, "up", heights[i][j]) or shortest(heights, i, j, "down", heights[i][j]) or \
                    shortest(heights, i, j, "left", heights[i][j]) or shortest(heights, i, j, "right", heights[i][j]):
                visible += 1
    return visible


def shortest(heights, i, j, direction, tree):
    """
    Check if the tree is the shortest in it a given direction
    :param heights: all the heights of trees in a multi-dimensional list
    :param i: row of the tree
    :param j: column of the tree
    :param direction: the direction to check
    :param tree: the height of the tree
    :return: True if the tree is the shortest in the given direction
    """
    # get the variables needed for the recursive function
    m, n, o = get_variables(heights, i, j, direction)

    if m[1] == m[0] and o < tree:
        return True
    if o >= tree:
        return False
    else:
        return shortest(n[0], n[1], n[2], direction, tree)


def scenic_score(heights):
    """
    Get the scenic score -> part 2 of day 8
    :param heights: all the heights of trees in a multi-dimensional list
    :return: the scenic score
    """
    columns = len(heights[0])
    rows = len(heights)
    part_score = 0
    score = 0
    # iterate over the trees in the middle
    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            # get the score for each tree and see if it is the highest
            temp = view(heights, i, j, "up", heights[i][j], part_score) * view(heights, i, j, "down", heights[i][j], part_score) * \
                    view(heights, i, j, "left", heights[i][j], part_score) * view(heights, i, j, "right", heights[i][j], part_score)
            if temp > score:
                score = temp
    return score


def view(heights, i, j, direction, tree, part_score):
    """
    Get the score for a given tree
    :param heights: all the heights of trees in a multi-dimensional list
    :param i: row of the tree
    :param j: column of the tree
    :param direction: the direction to check
    :param tree: the height of the tree
    :param part_score: the score of the tree
    :return: the score of the tree
    """
    # get the variables needed for the recursive function
    m, n, o = get_variables(heights, i, j, direction)
    # if the tree is smaller than the next one, keep counting
    if o < tree and m[1] != m[0]:
        part_score += 1
        return view(n[0], n[1], n[2], direction, tree, part_score)
    else:
        part_score += 1
        return part_score


def get_variables(heights, i, j, direction):
    """
    Get the variables needed for the recursive function
    :param heights: all the heights of trees in a multi-dimensional list
    :param i: row of the tree
    :param j: column of the tree
    :param direction: the direction to check
    :return: the variables needed for the recursive function
    """
    match direction:
        case "up":
            return (i, 1), [heights, i - 1, j], heights[i - 1][j]
        case "down":
            return (i, len(heights) - 2), [heights, i + 1, j], heights[i + 1][j]
        case "left":
            return (1, j), [heights, i, j - 1], heights[i][j - 1]
        case "right":
            return (len(heights[0]) - 2, j), [heights, i, j + 1], heights[i][j + 1]
        case _:
            return 0, 0, 0
