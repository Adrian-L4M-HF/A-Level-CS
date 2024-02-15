"""
•Q1. Refactor the class in order to remove the top attribute.

•Q2. Add a top method, which returns the top item without removing it.

•Q3. Write a short paragraph explaining your answers to Q1 and Q2.

"""

class stack:
    def __init__(self, size):
        self.maxsize = size
        self.__items = [0] * size

    def __len__(self):
        for index, item in enumerate(self.__items):
            if item == 0:
                return index
        return self.maxsize
    
    def top(self):
        if self.__len__() != 0:
            return self.__items[self.__len__()-1]
        else:
            return None
    
    def push(self, item):
        if self.__len__() == self.maxsize:
            raise IndexError('Stack Overflow')
        else:
            self.__items[self.__len__()] = item
    
    def pop(self):
        if self.__len__() - 1 < 0:
            raise IndexError('Stack Underflow')
        else:
            item = self.__items[self.__len__()-1]
            self.__items[self.__len__()-1] = 0
            return item

stk = stack(3)

stk.top()
stk.push(1)
stk.push(2)
stk.push(3)

assert len(stk) == 3
stk.top()
assert stk.pop() == 3
assert stk.pop() == 2
assert stk.pop() == 1

assert len(stk) == 0
stk.top()
print("PASS")


"""
For Q1
In the __len__(), the loops through the items list and yeilding
each item and their index at the same time. By checking the value of item (see
if it is "0"), the length will be the index (due to zero indexing).
If the stack is full (i.e. no "0" found), the maxsize is returned.

In push() and pop(), top is now being replaced by __len__() and __len()__() - 1
In pop(), when the top item is popped, its value is overidden by a "0".

For Q2
Top() checks the length of the list by using __len__(). If length is not "0", return
the top item but doesn't remove anything. If the list is empty (i.e. length is "0"),
then return None.
"""