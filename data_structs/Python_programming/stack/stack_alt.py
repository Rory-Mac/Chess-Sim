if __name__ == "__main__":
    stack = []
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
            stack.append(value)
        elif instruction == "pop":
            if not stack:
                print("cannot pop from empty stack")
            else:
                print(str(stack.pop()))
        elif instruction == "peek":
            print(stack[len(stack) - 1])
        elif instruction == "isempty":
            print("false" if stack else "true")
        elif instruction == "help":
            print("\tpush [value] : push to stack")
            print("\tpop : pop from stack")
            print("\tpeek : peek top element")
            print("\tisempty : print if empty")
            print("\thelp : list valid commands")
            print("\texit : exit interface")
        elif instruction == "exit":
            break
