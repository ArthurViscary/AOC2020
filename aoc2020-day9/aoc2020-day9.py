from itertools import combinations

with open('aoc2020-day9input.txt') as file:
    data = [int(line.strip()) for line in file.readlines()]

#in retrospect, deque from itertools would have been good for this
#target container for 25-sized number-blocks
blocks = []
start = 0
end = 26
block = []

while end < len(data):   
    for i in range(start,end):
        block.append(int(data[i]))
    blocks.append(block)
    block = []
    start += 1
    end += 1

def pt1_solver(input:list) -> int:
    for block in input:
        number = block[-1]
        combs = combinations(block[:-1],2)
        sums = []
        for comb in combs:
            sums.append(sum(comb))
        if number not in sums:
            print(number)
            break
        else:
            sums = []

pt1_solver(blocks)
