class Heap(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = [None] * max_size
        self.size = 0
    
    def heapify(self, i):
        root = self.items[i]
        left_child, left_child_i = self.get_left_child(i)
        right_child, right_child_i = self.get_right_child(i)
        max_child_i = left_child_i if left_child > right_child else right_child_i
        max_child = self.items[max_child]
        if max_child > root:
            self.items[i] = max_child
            self.items[max_child_i] = root 
            self.heapify(max_child)

    def get_parent(self, i):
        return (i - 1) // 2

    # returns left child and left child index
    def get_left_child(self, i):
        return self.items[2 * i + 1], 2 * i + 1

    # returns right child and right child index
    def get_right_child(self, i):
        return self.items[2 * i + 2], 2 * i + 2

    def insert(self, n):
        pass

    def remove(self, n):
        pass