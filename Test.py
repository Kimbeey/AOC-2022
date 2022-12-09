import Day08
import convert

# get the input
my_file = open('C:/Users/Kimi/Documents/Advent of code/08input.txt', 'r')

# try code for day 8
L = convert.list_of_list(my_file)
res = Day08.scenic_score(L)
print(res)


