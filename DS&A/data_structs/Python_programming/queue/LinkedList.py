class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self, value):
        node = LinkedListNode(value)
        if self.tail == None:
            self.head = node
            self.tail = node
            return
        self.tail.setNext(node)
        self.tail = node

    def dequeue(self):
        if self.head == None: return
        value = self.head.getValue()
        self.head = self.head.getNext()
        return value

    def printList(self):
        if (self.head == None): return
        curr = self.head
        while (curr != None):
            print(f"{curr.getValue()} ", end="")
            curr = curr.getNext()
        print()

    def reverse(self):
        if self.head == None or self.head.getNext() == None: return
        self.tail = self.head
        prev = None
        curr = self.head
        next = curr.getNext()
        while (curr != None):
            next = curr.getNext()
            curr.setNext(prev)
            prev = curr
            curr = next
        self.head = prev

class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def getValue(self):
        return self.value

if __name__ == "__main__":
    linkedList = LinkedList()
    while(True):
        command = input("Input instruction: ")
        instruction_words = command.split()
        instruction = None
        values = []
        if len(instruction_words) == 0:
            print("No instruction provided")
        elif len(instruction_words) == 1:
            instruction = instruction_words[0]
        elif len(instruction_words) > 1:
            instruction = instruction_words[0]
            values = instruction_words[1:]
        if instruction == "enqueue":
            for value in values:
                linkedList.enqueue(value)
        elif instruction == "dequeue":
            print(str(linkedList.dequeue()))
        elif instruction == "reverse":
            linkedList.reverse()
        elif instruction == "print":
            linkedList.printList()
        elif instruction == "help":
            print("\tenqueue [value] : enqueue element to list")
            print("\tdequeue : dequeue element from list")
            print("\treverse : reverse linked list")
            print("\tprint : print list")
            print("\thelp : list valid commands")
            print("\texit : exit interface")
        elif instruction == "exit":
            break
        else:
            print("command unkown, type 'help' to list valid commands")