#the list is formed as entries ending in empty newlines
#in order to separate the entries
with open("aoc2020-day4input.txt") as input:
    data = input.read().split("\n\n")

def validity_checker(passport:str) -> bool:
    fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for item in fields:
        if item not in passport:
            return False
    return True

valid_passports = 0
for passport in data:
    if validity_checker(passport):
        valid_passports += 1
print(valid_passports)
