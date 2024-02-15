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

G = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B", "D", "E"],
    "D": ["C", "E"],
    "E": ["C", "D", "F"],
    "F": ["E"],
}

goal = "F"

def BFS(G, root):
    Q = queue()
    explored = [root]
    Q.enqueue(root)
    while Q.is_empty() != True:
        v = Q.dequeue()
        if v == goal:
            return v
        for i in G.adjacentEdges(v):
            for j in i:
                if w not in explored:
                    explored.append(w)
                    w.parent = v
                    Q.enqueue(w)
