# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr=head
        prev=None
        while curr is not None:
            nextnode=curr.next #next node of the linked list
            curr.next=prev # reverses the list by changing the pointer to previous node
            prev=curr #moves the prev node ahead
            curr=nextnode # move the curr node ahead
        return prev
        