class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = [0] * capacity
        self.back = 0

    def get(self, i : int) -> int:
        return self.items[i]

    def set(self, i : int, n: int) -> int:
        self.items[i] = n

    def pushback(self, n : int) -> None:
        if self.back >= self.capacity:
            self.resize()
        self.items[self.back] = n
        self.back += 1

    def popback(self) -> int:
        if self.back == 0: return
        self.back -= 1
        item = self.items[self.back]
        return item

    def resize(self) -> None:
        self.items += [0] * self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.back

    def getCapacity(self) -> int:
        return self.capacity