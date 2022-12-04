import Day04
import convert

# get the input
my_file = open('C:/Users/Kimi/Documents/Advent of code/04input.txt', 'r')

# try code for day 3
L = convert.get_lis(my_file)
print(L)
print(Day04.get_total_overlaps(L))

