from linked_list import LinkedNode, LinkedList

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        next=None
        c_n_1=list1
        c_n_2=list2
        while c_n_1:
            while c_n_2:
                if c_n_1==c_n_2:
                    c_n_2=c_n_2.next
                elif c_n_2>c_n_1:
                    next=c_n_2.next
                    c_n_2.next=c_n_1
                    c_n_2=next
            c_n_1=c_n_1.next

        return c_n_2
    
if __name__=="__main__":
    list1=[1, 2, 4]
    list2=[2, 3, 4]

    linked_list1=LinkedList(list1)
    linked_list2=LinkedList(list2)

    solution=Solution()
    solution.mergeTwoLists(linked_list1, linked_list2)




