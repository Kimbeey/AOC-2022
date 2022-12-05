import Day05
import convert

# get the input
my_file = open('C:/Users/Kimi/Documents/Advent of code/05input.txt', 'r')

# try code for day 3
cargo, L = convert.lists_for_moves(my_file)
print(L, cargo)
res = Day05.rearrange_part2(cargo, L)
print(res)

for i in res:
    print(i[-1])
