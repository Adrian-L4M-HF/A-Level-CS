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

    def insertion_sort(self, items): # Q1
        pass
    
    def linear_search(self, item): # Q2
        for index, number in enumerate(self):
            if number == item:
                print(f"{item} is at index {index} in {self}")

ll = linked_list()

ll.insertion_sort([13, 2, 1, 8, 1, 0 ,3])

assert str(ll) == '0 1 1 2 3 8 13 '

print('PASS')