"""
•Q1. Explain the best and worst-case time-complexity of insertion sort.

Best Case:
Input list already sorted. 
Head iterates through the list once, so O(n)

Worst Case:
Input list in reverse order. 
Head iterates through the list once to compare items O(n)
swapping each item to their correct position O(n)
Hence, total is O(n^2) 

•Q2. Explain the best and worst-case time-complexity of linear search.

Best Case:
The first item in the list is the target item, so O(1)

Worst Case:
Target item is the last item in the list or
target item is not in list.
All items in the list are examined once, so O(n)

•Q3. Explain the differences between singly and doubly linked lists.

Singly Linked List:
Each node has two fields, data and next. 
Traversal is only possible in one direction using next link.
Less memory required than doubly linked list, since no "previous" field.
When deleting a node, previous node has to be identified, time complexity O(n)

Doubly Linked List:
Each node has three fields, data, previous and next.
Traversal is possible in both direction using next link or previous link.
More memory required than singly linked list, since there are "previous" fields.
When deleting a node, previous node can be accessed, time complexity O(1)

•Ext. Refactor the class into a doubly linked list.
"""
class node:
    def __init__(self, previous, data, next):
        self.previous = previous
        self.data = data
        self.next = next

class doubly_linked_list:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        head = self.head
        string = ''
        while head != None:
            string += f'{head.data} '
            head = head.next
        return string

    def insertion_sort(self, items: list): # A1
        for index, item in enumerate(items):
            previous = index - 1
            if previous == 0:
                previous = None
            new = node(previous, item, None)
            if self.head is None or self.head.data > item:
                new.next = self.head
                self.head = new
            else:
                prev = self.head
                curr = self.head.next
                while curr != None and curr.data <= item:
                    prev = curr
                    curr = curr.next
                prev.next = new
                new.next = curr
    
    def linear_search(self, item): # A2
        head = self.head
        while head != None:
            if head.data == item:
                return head
            head = head.next
        return None

ll = doubly_linked_list()

ll.insertion_sort([13, 2, 1, 8, 1, 0 ,3])

assert str(ll) == '0 1 1 2 3 8 13 '

print(f"{ll.linear_search(5) = }")
print(f"{ll.linear_search(2) = }")


print('PASS')