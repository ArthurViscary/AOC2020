from collections import Counter

with open("aoc2020-day6input.txt") as input:
    data = input.read().split("\n\n")

sum = 0


#notice: every line but one had a newline char, which we want to ignore
for line in data:
    if '\n' not in Counter(line):
        sum += 1
    sum += len(Counter(line)) - 1
