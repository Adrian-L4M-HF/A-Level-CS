class stack:
    def __init__(self, size):
        self.maxsize = size
        self.top = 0
        self.__items = [0] * size

    def __len__(self):
        return self.top
    
    def push(self, item):
        if self.top == self.maxsize:
            raise IndexError('Stack Overflow')
        else:
            self.__items[self.top] = item
            self.top = self.top + 1
    
    def pop(self):
        if self.top == 0:
            raise IndexError('Stack Underflow')
        else:
            self.top = self.top - 1
            item = self.__items[self.top]
            return item

stk = stack(3)

stk.push(1)
stk.push(2)
stk.push(3)

assert len(stk) == 3

assert stk.pop() == 3
assert stk.pop() == 2
assert stk.pop() == 1

assert len(stk) == 0

print("PASS")
