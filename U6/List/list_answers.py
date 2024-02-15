class node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class linked_list:
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
        for item in items:
            new = node(item, None)
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

ll = linked_list()

ll.insertion_sort([13, 2, 1, 8, 1, 0 ,3])

assert str(ll) == '0 1 1 2 3 8 13 '

print('PASS')