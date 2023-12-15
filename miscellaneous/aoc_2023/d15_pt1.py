def custom_hash(word):
    curr_val = 0
    for c in word:
        curr_val += ord(c)
        curr_val *= 17
        curr_val %= 256
    return curr_val

sum = 0
file = open('d15_input.txt', 'r')
curr_word = ""
while True:
    c = file.read(1)
    if not c:
        sum += custom_hash(curr_word)
        break
    if c == ",":
        sum += custom_hash(curr_word)
        curr_word = ""
    else:
        curr_word += c
print(sum)