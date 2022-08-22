

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            return print("Stack is empty")
        else:
            return self.stack.pop()

    def traverse(self):
        if self.stack == []:
            return print("Stack is empty")
        else:
            return self.stack[::-1]
