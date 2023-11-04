class Set:
    def __init__(self, items=[]):
        self.size = 0
        self.items = {}
        for item in items:
            self.addItem(item)

    def addItem(self, item):
        self.items[item] = item

    def discardItem(self, item):
        self.items.pop(item)

    def hasItem(self, item):
        return self.items.get(item) != None

    def print(self):
        for item in self.items:
            print(f"{item} ", end="")
        print()

    def intersection(self, set):
        key_set1 =  list(self.items.keys())
        key_set2 = list(set.items.keys())
        key_set1.sort()
        key_set2.sort()
        key_index1 = 0
        key_index2 = 0
        intersecting_items = []
        while key_index1 < len(key_set1) and key_index2 < len(key_set2):
            if key_set1[key_index1] == key_set2[key_index2]:
                intersecting_items.append(key_set1[key_index1])
                key_index1 += 1
                key_index2 += 1
                continue
            elif key_set1[key_index1] < key_set2[key_index2]:
                key_index1 += 1
            elif key_set1[key_index1] > key_set2[key_index2]:
                key_index2 += 1
        return intersecting_items

    def union(self, set):
        key_set1 =  list(self.items.keys())
        key_set2 = list(set.items.keys())
        key_set1.sort()
        key_set2.sort()
        key_index1 = 0
        key_index2 = 0
        union_items = []
        while key_index1 < len(key_set1) and key_index2 < len(key_set2):
            if key_set1[key_index1] == key_set2[key_index2]:
                union_items.append(key_set1[key_index1])
                key_index1 += 1
                key_index2 += 1
                continue
            elif key_set1[key_index1] < key_set2[key_index2]:
                union_items.append(key_set1[key_index1])
                key_index1 += 1
            elif key_set1[key_index1] > key_set2[key_index2]:
                union_items.append(key_set2[key_index2])
                key_index2 += 1
        while key_index1 < len(key_set1):
            union_items.append(key_set1[key_index1])
            key_index1 += 1
        while key_index2 < len(key_set2):
            union_items.append(key_set2[key_index2])
            key_index2 += 1
        return union_items
    
    def difference(self, set):
        key_set1 =  list(self.items.keys())
        key_set2 = list(set.items.keys())
        key_set1.sort()
        key_set2.sort()
        key_index1 = 0
        key_index2 = 0
        difference_items = []
        while key_index1 < len(key_set1) and key_index2 < len(key_set2):
            if key_set1[key_index1] == key_set2[key_index2]:
                key_index1 += 1
                key_index2 += 1
                continue
            elif key_set1[key_index1] < key_set2[key_index2]:
                difference_items.append(key_set1[key_index1])
                key_index1 += 1
            elif key_set1[key_index1] > key_set2[key_index2]:
                key_index2 += 1
        while key_index1 < len(key_set1):
            difference_items.append(key_set1[key_index1])
            key_index1 += 1
        return difference_items

if __name__ == "__main__":
    set1 = Set()
    set2 = Set()
    for i in range(5,10):
        set1.addItem(i)
    for i in range(5,10):
        set1.discardItem(i)
    for i in range(0,7):
        set1.addItem(i)
    for i in range(4,10):
        set2.addItem(i)
    # set1 (0,1,2,3,4,5,6), set2 (4,5,6,7,8,9)
    assert set1.union(set2) == [0,1,2,3,4,5,6,7,8,9]
    assert set2.union(set1) == [0,1,2,3,4,5,6,7,8,9]
    assert set1.intersection(set2) == [4,5,6]
    assert set2.intersection(set1) == [4,5,6]
    assert set1.difference(set2) == [0,1,2,3]
    assert set2.difference(set1) == [7,8,9]