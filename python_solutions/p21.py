# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val<=list2.val:  #checks whichever node is smaller
                current.next = list1 #attaches the node we compared to the merge list
                list1=list1.next  # moves the node to next node
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next

        current.next = list1 or list2  #whichever s=is not meppty will be added

        return dummy.next #not dummy because the actual list starts from dummy.next, dummy stored temporary node
        
        