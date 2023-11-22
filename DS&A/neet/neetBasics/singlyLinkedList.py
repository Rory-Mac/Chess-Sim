from typing import List

class LinkedListNode():
    def __init__(self, item : int, next=None):
        self.item = item
        self.next = next

class LinkedList:    
    def __init__(self):
        self.head = LinkedListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.item
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = LinkedListNode(val, self.head.next)
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        self.tail.next = LinkedListNode(val)
        self.tail = self.tail.next 

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while curr and i < index:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        items = []
        i = 0
        curr = self.head.next
        while curr:
            items.append(curr.item)
            i += 1
            curr = curr.next
        return items
