
with open("aoc2020-day1input.txt") as input:
    data = input.readlines()
    data = [int(line.strip()) for line in data]

def part1_checker(data:list) -> int:
    for i in data:
        for j in data:
            if i + j == 2020:
                return(i * j)

def part2_checker(data:list) -> int:
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    return i * j * k


    