class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        n = len(self.items)
        return n == 0

    def peek(self):
        x = None
        if not self.is_empty():
            top = -1 #solo para hacer el peek
            x = self.items[top]
        return x

    def push(self,x):
        self.items.append(x)

    def pop(self):
        x = None
        if not self.is_empty():
            top = -1
            x = self.items[top]
            del self.items[top]
        return x

