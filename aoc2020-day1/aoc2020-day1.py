import re
from collections import Counter

with open("aoc2020-day1input.txt") as input:
    data = input.readlines()
    data = [line.strip() for line in data]

#part1
def checker(data:list) -> int:
    count = 0
    for row in data:
        result_groups = re.search(r"(\d+)-(\d+) (\w): (\w+)", row)
        row_as_counter = Counter(result_groups.group(4))
        if row_as_counter[result_groups.group(3)] >= int(result_groups.group(1)) and row_as_counter[result_groups.group(3)]<= int(result_groups.group(2)):
            count += 1
    return count

#part2
def part2_checker(data:list) -> int:
    count = 0
    for row in data:
        result_groups = re.search(r"(\d+)-(\d+) (\w): (\w+)", row)
        positions = 0
        index1 = int(result_groups.group(1)) - 1
        index2 = int(result_groups.group(2)) - 1
        char = result_groups.group(3)
        password = result_groups.group(4)
        if password[index1] == char:
            positions += 1
        if password[index2] == char:
            positions += 1
        if positions == 1:
            count += 1
    return count

print(part2_checker(data))
