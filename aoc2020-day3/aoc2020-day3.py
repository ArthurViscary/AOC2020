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

#part 2
def part2_checker(data:list) -> int:
    slope_variations = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    tree_count_totals = []
    def tree_counter(data:list, slope_variation:list) -> int:
        tree_count = 0
        row, column = 0,0
        while row + 1 < len(data):
            row += int(slope_variation[1])
            column += int(slope_variation[0])
    
            space = data[row][column % len(data[row])]
            if space == "#":
                tree_count += 1 
        return tree_count
    for slope in slope_variations:
        tree_count_totals.append(tree_counter(data, slope))
    final_totals = 1
    for item in tree_count_totals:
        final_totals *= item
    return final_totals

