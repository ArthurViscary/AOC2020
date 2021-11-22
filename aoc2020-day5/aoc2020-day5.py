with open("aoc2020-day5input.txt") as input:
    data = input.readlines()
    data = [line.strip() for line in data]

print(data)

def part1_checker(data:list) ->int:
    highest = 0
    row = 0
    col = 0
    for line in data:
        low = 0
        high = 127
        for i in range(6):
            if line[i] == "F":
                high = low + (high - low) // 2
            elif line[i] == "B":
                low = low + (high + 1 - low) // 2
        if line[6] == "F":
            row = low
        else:
            row = high
        low, high = 0,7
        for i in range(7,9):
            if line[i] == "L":
                high = low + (high - low) // 2         
            elif line[i] == "R":
                low = low + (high + 1 - low) // 2          
        if line[9] == "L":
            col = low
        else: 
            col = high
        if row * 8 + col >= highest:
            highest = row * 8 + col

    return highest


print(part1_checker(data))

#part 2
id_list = []
row = 0
col = 0
for line in data:
    low = 0
    high = 127
    for i in range(6):
        if line[i] == "F":
            high = low + (high - low) // 2
        elif line[i] == "B":
            low = low + (high + 1 - low) // 2
    if line[6] == "F":
        row = low
    else:
        row = high
    low, high = 0,7
    for i in range(7,9):
        if line[i] == "L":
            high = low + (high - low) // 2         
        elif line[i] == "R":
            low = low + (high + 1 - low) // 2          
    if line[9] == "L":
        col = low
    else: 
        col = high
    id_list.append(row * 8 + col)

id_list.sort()

print(id_list)

def part2_checker(id_list:list) ->int:
    for id in id_list:
        if id+1 not in id_list and id+2 in id_list:
            return id+1

print(part2_checker(id_list))

