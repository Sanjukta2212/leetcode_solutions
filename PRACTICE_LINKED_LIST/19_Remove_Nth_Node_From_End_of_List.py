# Given the head of a linked list, remove the nth node from the end of the list and return its head.
class Linked_Node():
    def __init__(self, value):
        self.value=value
        self.next=None

    def __repr__(self):
        return str(self.head)
    
class LinkedList():
    def __init__(self, *values):
        self.head=None
        for value in values[::-1]:
            self.insert_at_begining(value)

    def insert_at_begining(self, value):
        current=self.head
        new_node=Linked_Node(value)
        new_node.next=current
        self.head=current

    def traverse(self):
        current=self.head
        while current:
            print("->",current.value)
            current=current.next

    def insert_at_index(self, n):
        ahead=self.head
        behind=self.head
        count=0
        while ahead:
            if count<n:
                ahead=ahead.next
                count+=1
            else:
                behind=behind.next
                ahead=ahead.next
                count+=1
        behind.next=behind.next.next

    
