# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.
class Linked_node():
    def __init__(self, value):
        self.value=value
        self.next=None

    def __repr__(self):
        return str(self.value)
    
class Linked_list():
    def __init__(self, *values):
        self.head=None
        for value in values[::-1]:
            self.insert_at_begining(value)

    def insert_at_begining(self, value):
        new_node=Linked_node(value)
        new_node.next=self.head
        self.head=new_node

    def traverse(self):
        current=self.head
        while current:
            print("->",current.value)
            current=current.next


    def middleNode(self):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=self.head
        fast=self.head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow)
        return slow
    

if __name__=="__main__":
    li=[1,2,3,4,5,6]
    l1_obj=Linked_list(*li)
    l1_obj.traverse()
    l1_obj.middleNode()
