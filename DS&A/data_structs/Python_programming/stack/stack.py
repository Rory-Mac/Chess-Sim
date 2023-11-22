class Stack:
    def __init__(self):
        self.top = -1
        self.values = []

    def push(self, value):
        self.top += 1
        self.values.append(value)
    
    def pop(self):
        if self.isempty():
            print("cannot pop from empty stack")
            return
        value = self.values[self.top] 
        del self.values[self.top]
        self.top -= 1
        return value 
    
    def peek(self):
        return self.values[self.top]
    
    def isempty(self):
        return self.top == -1
    
def test_stack(stack):
    for i in range(1000):
        stack.push(i)
    for i in range(1000):
        assert stack.pop() == 999 - i

if __name__ == "__main__":
    stack = Stack()
    while(True):
        command = input("Input instruction: ")
        instruction_words = command.split()
        instruction = None
        value = None
        if len(instruction_words) == 0:
            print("Invalid instruction format")
        elif len(instruction_words) == 1:
            instruction = instruction_words[0]
        elif len(instruction_words) == 2:
            instruction = instruction_words[0]
            value = instruction_words[1]
        if instruction == "push":
            stack.push(value)
        elif instruction == "pop":
            popped_elem = stack.pop()
            if popped_elem != None:
                print(str(popped_elem))
        elif instruction == "peek":
            print(str(stack.peek()))
        elif instruction == "isempty":
            print(str(stack.isempty()))
        elif instruction == "help":
            print("\tpush [value] : push to stack")
            print("\tpop : pop from stack")
            print("\tpeek : peek top element")
            print("\tisempty : print if empty")
            print("\thelp : list valid commands")
            print("\texit : exit interface")
        elif instruction == "exit":
            break
    test_stack(stack)
