import random
class Store:
    def __init__(self, initial_items=[]):
        self.items = []
        self.item_indices = {}
        self.addItems(initial_items)

    def addItem(self, item):
        self.items.append(item)
        self.item_indices[item] = len(self.items) - 1
    
    def addItems(self, items):
        for item in items:
            self.addItem(item)

    def removeItem(self, item):
        if self.item_indices.get(item, None) == None: return
        item_index = self.item_indices.pop(item)
        if item_index == len(self.items) - 1:
            self.items.pop()
        else:
            migrated_item = self.items.pop()
            self.items[item_index] = migrated_item 
            self.item_indices[migrated_item] = item_index

    def removeItems(self, items):
        for item in items:
            self.removeItem(item)

    def getRandomItem(self):
        return random.choice(self.items)
    
if __name__ == "__main__":
    mySet = Store([13,8,9,3,4,7,11,5,10,2,1,6,12])
    mySet.removeItems([12,13,14,15])
    for _ in range(0,10):
        print(f"{mySet.getRandomItem()} ", end="")
    print()
