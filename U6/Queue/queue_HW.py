"""
•Q1. Add an is_empty method that returns whether the queue is empty.

•Q2. Add an is_full method that returns whether the queue is full.

•Q3. Add a peek method that returns the first item without dequeuing it.

•Ext. Refactor the class into a circular queue.
"""
class queue:
    def __init__(self, size):
        self.maxsize = size
        self.__items = []
    
    def __len__(self):
        return len(self.__items)

    def is_empty(self):
        if len(self) == 0:
            return True

    def is_full(self):
        if len(self) == self.maxsize:
            return True 

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        else:
            return self.__items[0]
    
    def enqueue(self, item):
        if self.is_full():
            raise IndexError('Queue Overflow')
        else:
            self.__items.append(item)
    
    def dequeue(self):
        first_item = self.peek()
        self.__items.remove(first_item)
        return first_item

def test1():
    que = queue(3)

    que.enqueue(1)
    que.enqueue(2)
    print(que.peek())
    que.enqueue(3)
    print(que.is_full())

    assert len(que) == 3

    assert que.dequeue() == 1
    assert que.dequeue() == 2
    print(que.peek())
    assert que.dequeue() == 3
    
    assert len(que) == 0
    print(que.is_empty())

    print("test 1 pass")

test1()

