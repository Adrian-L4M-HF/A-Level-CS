class queue:
    def __init__(self, size):
        self.maxsize = size
        self.__items = []
    
    def __len__(self): # A1
        return len(self.__items)
    
    def enqueue(self, item): # A2
        if len(self) == self.maxsize:
            raise IndexError('Queue Overflow')
        else:
            self.__items.append(item)
    
    def dequeue(self): # A3
        if len(self) == 0:
            raise IndexError('Queue Underflow')
        else:
            return self.__items.pop(0)

def test1():
    que = queue(3)

    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)

    assert len(que) == 3

    assert que.dequeue() == 1
    assert que.dequeue() == 2
    assert que.dequeue() == 3

    assert len(que) == 0

    print("test 1 pass")

def test2():
    que = queue(-3) #It should not allow negative number
    que.enqueue(1)
    que.enqueue(2)
    assert len(que) == 2
    for i in range(3):
        que.enqueue(3)
    print(f"{len(que)=}")
    for j in range(5):
        que.dequeue()
    print("test 2 pass")

test1()
test2()
