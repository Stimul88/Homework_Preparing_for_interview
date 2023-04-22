class Stack:

    def __init__(self):
        self.brack = []

    def is_empty(self):
        return len(self.brack) == 0

    def push(self, item):
        self.brack.append(item)

    def pop(self):
        return self.brack.pop()

    def peek(self):
        return self.brack[-1]

    def size(self):
        return len(self.brack)