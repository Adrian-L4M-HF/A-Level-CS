class queue:
    def __init__(self, size):
        self.maxsize = size
        self.__items = []
    
    def __len__(self): # Q1
        return len(self.__items)
    
    def enqueue(self, item): # Q2
        self.__items.append(item)
    
    def dequeue(self): # Q3
        item = self.__items[0]
        self.__items = self.__items[1:len(self.__items)]
        return item

que = queue(3)

que.enqueue(1)
que.enqueue(2)
que.enqueue(3)

assert len(que) == 3

assert que.dequeue() == 1
assert que.dequeue() == 2
assert que.dequeue() == 3

assert len(que) == 0

print("PASS")