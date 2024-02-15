class CircularQueue():
    
     def __init__(self, maxSize):
         """To initialise the queue"""
         self.front = 0
         self.rear = -1
         self.size = 0
         self.maxSize = maxSize
         self.q = [None] * maxSize
    
     def isEmpty(self):
         """To test for an empty queue"""
         if self.size == 0:
            return True
         else:
            return False

     def isFull(self):
         """To test for a full queue"""
         if self.size == self.maxSize:
            return True
         else:
            return False

     def enqueue(self, newItem):
         """To add an element to the queue"""
         if CircularQueue.isFull(self):
            print("Queue full")
         else:
            self.rear = (self.rear + 1) % self.maxSize
            self.q[self.rear] = newItem
            self.size += 1
        
     def dequeue(self, item):
         """To remove an item from the queue"""
         if CircularQueue.isEmpty(self):
            print("Queue empty")
         else:
            item = self.q[self.front]
            self.front = (self.front + 1) % self.maxSize
            self.size -= 1
         return item
     def __str__(self):
         return f'CircularQueue.q = {self.q}'

#Test
queue = CircularQueue(5)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(6)
queue.dequeue(3)
queue.enqueue(8)
queue.enqueue(10)
queue.dequeue(4)
print(queue.q)





