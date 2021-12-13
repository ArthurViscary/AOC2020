from collections import Counter

with open("aoc2020-day6input.txt") as input:
    data = input.read().split("\n\n")

sum = 0


#notice: every line but one had a newline char, which we want to ignore
for line in data:
    if '\n' not in Counter(line):
        sum += 1
    sum += len(Counter(line)) - 1


#pt2
def pt2_solver(data:list[str]) -> int:
    pt2_sum = 0
    for line in data:
        answers = len(line.split('\n'))
        line_counter = Counter(line)
        for char in line_counter:
            if char != '\n' and line_counter.get(char) == answers:
                pt2_sum += 1
    return pt2_sum


print(pt2_solver(data))