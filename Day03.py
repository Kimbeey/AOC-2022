def get_prio(rucksacks):
    """
    Part 1 of day 2
    :param rucksacks: list of contents from the rucksacks
    :return: sum of the priorities of the item type that appears in both compartments of each rucksack
    """
    prio = 0
    for items in rucksacks:
        x = len(items)
        # separate the contents in half
        comp1 = items[0:x//2]
        comp2 = items[x//2:]
        # find the item that is in both compartments
        mistake = ''.join(set(comp1).intersection(comp2))
        # compute the priority and add to the end result
        prio += ord(mistake) - 96 if mistake.islower() else ord(mistake) - 38

    return prio


def get_groups(rucksacks):
    """
    Part 2 of day 2
    :param rucksacks: list of contents from the rucksacks
    :return: sum of the priorities of the item type that corresponds to the badges of each three-Elf group
    """
    prio = 0
    for i in range(0, len(rucksacks), 3):
        # get a list of the three rucksacks
        elves = [rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]]
        # get the item that appears in all three rucksacks
        mistake = ''.join(set.intersection(*map(set, elves)))
        prio += ord(mistake) - 96 if mistake.islower() else ord(mistake) - 38

    return prio
