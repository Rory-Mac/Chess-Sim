myDictionary = dict.fromkeys(["apple", "banana", "orange"], "fruits")
myDictionary.update(dict.fromkeys(["brocolli", "cauliflower"], "vegetables"))

print(myDictionary["apple"])
print(myDictionary["banana"])
print(myDictionary["orange"])
print(myDictionary["brocolli"])
print(myDictionary["cauliflower"])