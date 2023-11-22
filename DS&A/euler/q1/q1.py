multiple_of_3 = 3
multiples_of_3 = [3]
multiple_of_5 = 5
sum = 0
while multiple_of_3 < 1000:
    sum += multiple_of_3
    multiples_of_3.append(multiple_of_3)
    multiple_of_3 += 3
while multiple_of_5 < 1000:
    if multiple_of_5 not in multiples_of_3:
        sum += multiple_of_5
    multiple_of_5 += 5
print(sum)