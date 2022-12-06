def get_start(code):
    """
    Part 1 for day 6. For part 2: replace n = 4 with n = 14
    :param code: datastream buffer
    :return: first position where the four most recently received characters were all different
    """
    start_pattern = set()
    n = 4
    for i in range(0, len(code)):
        counter = 0
        for j in range(i, i + n):
            start_pattern.add(code[j])
            counter += 1
            if len(start_pattern) < counter:
                start_pattern = set()
                break
            if len(start_pattern) == n:
                return j + 1
    return None