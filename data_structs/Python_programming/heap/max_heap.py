class Heap(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = [None] * max_size
        self.size = 0

    # returns parent item and parent index
    def parent_index(self, i):
        return (i - 1) // 2

    # returns left child and left child index
    def left_child_index(self, i):
        return 2 * i + 1

    # returns right child and right child index
    def right_child_index(self, i):
        return 2 * i + 2
    
    # bubble up element indexed by i
    def bubble_up(self, i):
        parent_i = self.parent_index(i)
        if parent_i < 0: return
        parent_item = self.items[parent_i]
        child_item = self.items[i]
        if child_item > parent_item:
            temp = child_item
            child_item = parent_item
            parent_item = temp
            self.bubble_up(self, parent_i)

    # bubble down element indexed by i
    def bubble_down(self, i):
        left_child_i = self.left_child_index(i)
        right_child_i = self.right_child_index(i)
        largest_i = left_child_i if self.items[left_child_i] > self.items[right_child_i] else right_child_i
        if self.items[largest_i] > self.items[i]:
            temp = self.items[i]
            self.items[i] = self.items[largest_i]
            self.items[largest_i] = temp
            self.bubble_down(largest_i)

    # get maximum element and remove from heap (constant time)
    def popMax(self):
        root_value = self.items[0]
        new_root_value = self.items[self.size - 1]
        root_value = new_root_value
        self.size -= 1
        self.bubble_down(0)
        return root_value

    # insert heap element (log2_n time)
    def insert(self, n):
        self.items.append(n)
        self.bubble_up(self, self.size - 1)
        self.size += 1

    # remove heap element (log2_n time)
    def remove(self, i):
        if i == self.size - 1: 
            self.size -= 1
            self.items.pop()
            return
        self.size -= 1
        self.items[i] = self.items.pop()
        parent_i = self.parent_index(i)
        if parent_i >= 0 and self.items[parent_i] < self.items[i]:
            self.bubble_up(i)
        else:
            self.bubble_down(i)