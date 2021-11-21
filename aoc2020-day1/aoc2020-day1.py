import re
from collections import Counter

with open("aoc2020-day1input.txt") as input:
    data = input.readlines()
    data = [line.strip() for line in data]

def checker(data:list) -> int:
    count = 0
    for row in data:
        result_groups = re.search(r"(\d+)-(\d+) (\w): (\w+)", row)
        row_as_counter = Counter(result_groups.group(4))
        if row_as_counter[result_groups.group(3)] >= int(result_groups.group(1)) and row_as_counter[result_groups.group(3)]<= int(result_groups.group(2)):
            count += 1
    return count

