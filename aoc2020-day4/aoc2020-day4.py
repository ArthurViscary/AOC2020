#the list is formed as entries ending in empty newlines
#in order to separate the entries
with open("aoc2020-day4input.txt") as input:
    data = input.read().split("\n\n")

#pt 1
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
#print(valid_passports)

def pt2_validity_checker(passport:str) -> bool:
    fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for item in fields:
        if item not in passport:
            return False
    for item in fields:
        if item == 'byr' and 'byr' < 1920 or 'byr' > 2002:
            return False
        if item == 'iyr' and 'iyr' < 2010 or 'iyr' > 2020:
            return False
        if item == 'eyr' and 'eyr'
    return True