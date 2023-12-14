fd = open('day_one_input.txt', 'r')
num_strs = {}
for i in range(10):
    num_strs[str(i)] = str(i)
sum = 0
for line in fd:
    lp = 0
    rp = -1
    while not num_strs.get(line[lp], None):
        lp += 1
    while not num_strs.get(line[rp], None):
        rp -= 1
    sum += int(line[lp] + line[rp])
print(sum)