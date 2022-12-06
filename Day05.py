from collections import deque


def rearrange(cargos, moves):
    """
    part 1 of day 5
    :param cargos: starting stacks of crates (as a list of deques)
    :param moves: rearrangement procedure (as a list of lists)
    :return: the stacks of crates after the rearrangement (as a list of deques)
    """
    stacks = []
    for level in reversed(cargos):
        for j in range(0, len(level)):
            if j + 1 > len(stacks):
                stacks += [deque([])]
            if level[j]:
                stacks[j].append(level[j])
    print(stacks)

    for elem in moves:
        for i in range(0, elem[0]):
            stack_to_remove = elem[1] - 1
            stack_to_add = elem[2] - 1
            temp = stacks[stack_to_remove][len(stacks[stack_to_remove]) - 1]
            stacks[stack_to_remove].pop()
            stacks[stack_to_add].append(temp)

    return stacks


def rearrange_part2(cargos, moves):
    """
    part 2 of day 5
    :param cargos: starting stacks of crates (as a list of deques)
    :param moves: rearrangement procedure (as a list of lists)
    :return: the stacks of crates after the rearrangement (as a list of deques)
    """
    stacks = []
    for level in reversed(cargos):
        for j in range(0, len(level)):
            if j + 1 > len(stacks):
                stacks += [deque([])]
            if level[j]:
                stacks[j].append(level[j])

    for elem in moves:
        num = elem[0]
        stack_to_remove = list(stacks[elem[1] - 1])
        temp = stack_to_remove[len(stack_to_remove) - num: len(stack_to_remove)]
        new_stack = stack_to_remove[:len(stack_to_remove) - num]
        stacks[elem[1] - 1] = new_stack
        stacks[elem[2] - 1] += temp
    return stacks
