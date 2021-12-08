with open("aoc2020-day8input.txt") as input:
    data = input.readlines()
    data = [line.strip() for line in data]


def part1_solver(data):
    visited = {}
    acc = 0
    index = 0

    while True:
        if str(index) in visited:
            return acc
        command = data[index]
        action, value = command.split(' ')
        if action == 'nop':
            visited.update({str(index) : 1})
            index += 1           
        elif action == 'acc':
            acc += int(value)
            visited.update({str(index) : 1})
            index += 1
        elif action == 'jmp':
            visited.update({str(index) : 1})
            index += int(value)
    
print(part1_solver(data))