class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)] # boolean array of len 26 representing storage of corresponding letter

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_words(self, words):
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        curr = self.root
        for c in word:
            child = curr.children[ord(c) - ord('a')]
            if child == None:
                curr.children[ord(c) - ord('a')] = TrieNode()
                curr = curr.children[ord(c) - ord('a')]
            else:
                curr = curr.children[ord(c) - ord('a')]

    def search_word(self, word):
        curr = self.root
        for c in word:
            child = curr.children[ord(c) - ord('a')]
            if child == None:
                return False
            curr = curr.children[ord(c) - ord('a')]
        return True
    
    def match_word(self, line, index):
        curr = self.root
        for c in line[index:-1]:
            if not (ord('a') <= ord(c) <= ord('z')): 
                return False
            child = curr.children[ord(c) - ord('a')]
            if child == None:
                return not any(curr.children)
            else:
                curr = curr.children[ord(c) - ord('a')]
        return True

# test trie functionality
my_trie = Trie()
str_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
my_trie.add_words(str_nums)
for str_num in str_nums:
    assert my_trie.search_word(str_num)
invalid_traversals = ["fanf", "onee", "eightnine", "teatot", "sixs"]
for traversal in invalid_traversals:
    assert not my_trie.search_word(traversal)
matching_lines = ["oneasdf", "twooooooo", "seven", "two1"]
for line in matching_lines:
    assert my_trie.match_word(line, 0)
unmatching_lines = ["onfjdaskl", "twwoooooo", "sseven"]
for line in unmatching_lines:
    assert not my_trie.match_word(line, 0)


str_num_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
str_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def which_number(word):
    if word[0] == "o":
        return "1"
    if word[0] == "t":
        if word[1] == "w":
            return "2"
        if word[1] == "h":
            return "3"
    if word[0] == "f":
        if word[1] == "o":
            return "4"
        if word[1] == "i":
            return "5"
    if word[0] == "s":
        if word[1] == "i":
            return "6"
        if word[1] == "e":
            return "7"
    if word[0] == "e":
        return "8"
    if word[0] == "n":
        return "9"
    return None

# main program
fd = open('eg.txt', 'r')
sum = 0
for line in fd:
    left = None
    right = None
    for i in range(len(line) - 3):
        if line[i] in str_num_digits:
            left = line[i]
            break
        elif my_trie.match_word(line, i):
            left = which_number(line[i:i+2])
            break
    for i in range(3, len(line)):
        if line[-i] in str_num_digits:
            right = line[-i]
            break
        elif my_trie.match_word(line, -i):
            right = which_number(line[-i:-i+2])
            break
    if left != None and right != None:
        sum += int(left + right)