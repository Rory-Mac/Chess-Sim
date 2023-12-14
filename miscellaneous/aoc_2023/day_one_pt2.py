import re

str_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def convert(word):
    if word[0] == "o":
        return "1"
    if word[0] == "e":
        return "8"
    if word[0] == "n":
        return "9"
    if word[0] == "t":
        if word[1] == "w":
            return "2"
        if word[1] == "h":
            return "3"
    if word[0] == "f":
        if word[1] == "i":
            return "5"
        if word[1] == "o":
            return "4"
    if word[0] == "s":
        if word[1] == "e":
            return "7"
        if word[1] == "i":
            return "6"

fd = open('day_one_input.txt', 'r')
sum = 0
for line in fd:
    first = None
    last = None
    for i, c in enumerate(line):
        discovered = None
        if c in str_nums:
            discovered = c
        match = re.match(r'one|two|three|four|five|six|seven|eight|nine', line[i:])
        if match:
            discovered = convert(match.group())
        if first == None:
            first = discovered
        if discovered:
            last = discovered
    if first and last:
        sum += int(first + last)
print(sum)