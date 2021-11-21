with open("aoc2020-day3input.txt") as input:
    data = input.readlines()
    data = [line.strip() for line in data]

tree_count = 0
row, column = 0,0

while row + 1 < len(data):
    row += 1
    column += 3
    
    space = data[row][column % len(data[row])]
    if space == "#":
        tree_count += 1

print(tree_count)