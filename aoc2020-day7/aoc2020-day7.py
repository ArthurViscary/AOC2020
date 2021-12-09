import re

with open('aoc2020-day7.txt') as f:
    data = [line.strip() for line in f.readlines()]

#regex tools for data parsing
first_bag_regex = r'^(\w+ \w+ bag)'
contain_bag_regex = r'(\d) (\w+ \w+ bag)'

#target container for parsed bag data
bag_dict = {}

#OOPing bags for data parsing
class Bag:
    def __init__(self, color, contains):
        self.color = color
        self.contains = contains

def data_parser(bag_data):
    parsed_bag_list = []
    for line in bag_data:
        color = str(re.findall(first_bag_regex, line))
        contains = {}
        for bag in re.findall(contain_bag_regex, line):
            contains.update({str(bag[1]).replace('bags','bag') : int(bag[0])})
        parsed_bag_list.append(Bag(color, contains))
    return parsed_bag_list

for bag in data_parser(data):
    bag_dict.update({bag.color : bag.contains})

#which bags can contain shiny gold bags?

eventual_sgb_containers = []

for item in bag_dict.items():
        if 'shiny gold bag' in item[1] and item[0][2:-2] not in eventual_sgb_containers:
            eventual_sgb_containers.append(item[0][2:-2])

#for breaking out of the while loop when no more eventual containers       
previous_len = len(eventual_sgb_containers)

#will loop as long as there are bags which eventually can contain shiny gold bags
while True:    
    for item in bag_dict.items():
        for bag in eventual_sgb_containers:
            if bag in item[1] and item[0][2:-2] not in eventual_sgb_containers:
                eventual_sgb_containers.append(item[0][2:-2])
    if len(eventual_sgb_containers) > previous_len:
        previous_len = len(eventual_sgb_containers)
        continue
    else:
        break

#print(eventual_sgb_containers)
#answer to part 1:
#print(len(eventual_sgb_containers))



