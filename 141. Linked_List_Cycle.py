class LinkedNode():
    def __init__(self, value):
          self.value=value
          self.next=None
    
    def __repr__(self):
        return self.value
    
class LinkedList():
    def __init__(self,*values):
        self.head=None
        for value in values[::-1]:
            self.insert_at_begining(value)

    def insert_at_begining(self):
        current_head=self.value
        new_node=LinkedNode(self.value)
        current_head.next=new_node
        self.head=new_node                             

    def hasCycle(head):
            """
            :type head: ListNode
            :rtype: bool
            """
            slow=head
            fast=head
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
                if slow==fast:
                    return True
            return False
                
    head=[3,2,0,-4]
    if __name__=="__main__":
        head=[3,2,0,-4]
        hasCycle(head)