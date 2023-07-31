
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         next=None
#         c_n_1=list1
#         c_n_2=list2
#         while c_n_1:
#             while c_n_2:
#                 if c_n_1==c_n_2:
#                     c_n_2=c_n_2.next
#                 elif c_n_2>c_n_1:
#                     next=c_n_2.next
#                     c_n_2.next=c_n_1
#                     c_n_2=next
#             c_n_1=c_n_1.next

#         return c_n_2


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
    for ele1, ele2 in zip(list1, list2):
            if list1.head<=list2.head:
                ptr1=list1.head
                ptr2=list2.head
                print(ptr1)
            else:
                ptr1=list2.head
                ptr2=list1.head
                print(ptr1)

            while ptr1 or ptr2 !=None:
                if ptr1.next>=ptr2:
                    ptr1.next=ptr2
                    ptr2.next=ptr1
                    print(ptr1)

                elif ptr1.next<ptr2:
                    ptr1=ptr1.next
                    print(ptr1)

                elif ptr1.next==ptr2:
                    prev_next=ptr1.next
                    ptr1.next=ptr2
                    ptr2.next=prev_next
                    print(ptr1)
    
if __name__=="__main__":
    list1=[1, 2, 4]
    list2=[2, 3, 4]

    linked_list1=LinkedList(list1)
    linked_list2=LinkedList(list2)

    solution=Solution()
    solution.mergeTwoLists(linked_list1, linked_list2)




