import Day03
import convert

# get the input
my_file = open('C:/Users/Kimi/Documents/Advent of code/03input.txt', 'r')

# try code for day 3
L = convert.get_lists(my_file)
print(L)
print(Day03.get_groups(L))
