def get_prio(rucksacks):
    prio = 0
    for items in rucksacks:
        x = len(items)
        comp1 = items[0:x//2]
        comp2 = items[x//2:]
        mistake = ''.join(set(comp1).intersection(comp2))
        prio += ord(mistake) - 96 if mistake.islower() else ord(mistake) - 38

    return prio


def get_groups(rucksacks):
    prio = 0
    for i in range(0, len(rucksacks), 3):
        elves = [rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]]
        mistake = ''.join(set.intersection(*map(set, elves)))
        prio += ord(mistake) - 96 if mistake.islower() else ord(mistake) - 38

    return prio
