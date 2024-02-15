class queue:
    def __init__(self):
        self.__items = []
    
    def __len__(self):
        return len(self.__items)
    
    def enqueue(self, item):
        self.__items.append(item)
    
    def dequeue(self):
        if len(self) == 0:
            raise IndexError('Queue Underflow')
        else:
            return self.__items.pop(0)
        
    def is_empty(self):
        return len(self) == 0

class stack:
    def __init__(self):
        self.__items = []
    
    def __len__(self):
        return len(self.__items)
    
    def push(self, item):
        self.__items.append(item)
    
    def pop(self):
        if len(self) == 0:
            raise IndexError('Stack Underflow')
        else:
            return self.__items.pop()
        
    def is_empty(self):
        return len(self) == 0

G = {
    'A': [ 'B', 'C' ],
    'B': [ 'A', 'C' ],
    'C': [ 'A', 'B', 'D', 'E' ],
    'D': [ 'C', 'E' ],
    'E': [ 'C', 'D', 'F' ],
    'F': [ 'E' ]
}

#  1  procedure BFS(G, root) is
#  2      let Q be a queue
#  3      label root as explored
#  4      Q.enqueue(root)
#  5      while Q is not empty do
#  6          v := Q.dequeue()
#  7          if v is the goal then
#  8              return v
#  9          for all edges from v to w in G.adjacentEdges(v) do
# 10              if w is not labeled as explored then
# 11                  label w as explored
# 12                  w.parent := v
# 13                  Q.enqueue(w)
# 
# Reference: https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode

root = 'A'
goal = 'F'
parents = {}

def BFS(G, root):
    Q = queue()
    explored: set = { root }
    Q.enqueue(root)
    # print(f'First Step: enqueue {root}')

    while not Q.is_empty():
        v = Q.dequeue()
        # print(f'Step 1: dequeue {v}')
        if v == goal:
            # print(f'Last Step: return {v}')
            return v
        for w in G[v]:
            # print(f'Step 2: from {v} to {w}')
            if not (w in explored):
                # print(f'Step 3: explore and enqueue {w}')
                explored.add(w)
                parents[w] = v
                Q.enqueue(w)

v = BFS(G, root)

while v != root:
    # print(f'Step from {v} to {parents[v]}')
    v = parents[v]

"""
Task 1. Implement a recursive-style depth-first search algorithm.
Task 2. Implement an iterative-style depth-first search algorithm.
Reference: https://en.wikipedia.org/wiki/Depth-first_search#
"""

"""recursive-style depth-first search algorithm"""
"""
procedure DFS(G, v) is
    label v as discovered
    for all directed edges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            recursively call DFS(G, w)
"""

discovered_nodes = set()
def DFS(G, v):
    for w in G[v]:
        if not (w in discovered_nodes):
            #print(f"{w = }")
            discovered_nodes.add(w)
            DFS(G, w)

#DFS(G, root)

"""iterative-style depth-first search algorithm"""

#Version 1
"""
procedure DFS_iterative(G, v) is
    let S be a stack
    S.push(v)
    while S is not empty do
        v = S.pop()
        if v is not labeled as discovered then
            label v as discovered
            for all edges from v to w in G.adjacentEdges(v) do 
                S.push(w)
"""

def DFS_iterative_1(G, v):
    discovered = set()
    S = stack()
    S.push(v)
    while not S.is_empty():
        v = S.pop()
        if not (v in discovered):
            #print(f"{v = }")
            discovered.add(v)
            for w in G[v]:
                S.push(w)

#DFS_iterative_1(G, root)




#Version 2
"""
procedure DFS_iterative(G, v) is
    let S be a stack
    label v as discovered
    S.push(iterator of G.adjacentEdges(v))
    while S is not empty do
        if S.peek().hasNext() then
            w = S.peek().next()
            if w is not labeled as discovered then
                label w as discovered
                S.push(iterator of G.adjacentEdges(w))
        else
            S.pop()
"""

def DFS_iterative_2(G, v):
    S = stack()
    discovered = set(v)
    for w in G[v]:
        S.push(w)
    while not S.is_empty():
        if S.peek().hasNext():
            w = S.peek().next()
            if not (w in discovered):
                print(w)
                discovered.add(w)
                S.push(w)
        else:
            S.pop()