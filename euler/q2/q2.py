t0 = 0
t1 = 1
sum = 0
while (t1 < 4000000):
    temp = t0
    t0 = t1
    t1 += temp
    if (t1 % 2 == 0):
        sum += t1
print(sum)