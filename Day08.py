def get_visible(heights):
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
    match direction:
        case "up":
            m = (i, 1)
            n = [heights, i-1, j]
            o = heights[i-1][j]
        case "down":
            m = (i, len(heights) - 2)
            n = [heights, i + 1, j]
            o = heights[i + 1][j]
        case "left":
            m = (1, j)
            n = [heights, i, j - 1]
            o = heights[i][j - 1]
        case "right":
            m = (len(heights[0]) - 2, j)
            n = [heights, i, j + 1]
            o = heights[i][j + 1]
        case _:
            m = 0
            n = 0
            o = 0

    if m[1] == m[0] and o < tree:
        return True
    if o >= tree:
        return False
    else:
        return shortest(n[0], n[1], n[2], direction, tree)


def scenic_score(heights):
    columns = len(heights[0])
    rows = len(heights)
    part_score = 0
    score = 0
    # iterate over the trees in the middle
    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            temp = view(heights, i, j, "up", heights[i][j],part_score) * view(heights, i, j, "down", heights[i][j], part_score) * \
                    view(heights, i, j, "left", heights[i][j], part_score) * view(heights, i, j, "right", heights[i][j], part_score)
            if temp > score:
                score = temp
    return score


def view(heights, i, j, direction, tree, part_score):
    match direction:
        case "up":
            m = (i, 1)
            n = [heights, i-1, j]
            o = heights[i-1][j]
        case "down":
            m = (i, len(heights) - 2)
            n = [heights, i + 1, j]
            o = heights[i + 1][j]
        case "left":
            m = (1, j)
            n = [heights, i, j - 1]
            o = heights[i][j - 1]
        case "right":
            m = (len(heights[0]) - 2, j)
            n = [heights, i, j + 1]
            o = heights[i][j + 1]
        case _:
            m = 0
            n = 0
            o = 0

    if m[1] == m[0] and o < tree:
        part_score += 1
        return part_score
    if o == tree:
        part_score += 1
        return part_score
    if o > tree:
        part_score += 1
        return part_score
    else:
        part_score += 1
        return view(n[0], n[1], n[2], direction, tree, part_score)