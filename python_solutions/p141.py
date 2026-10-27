# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast is not None and fast.next is not None: #run untill fast and next node of fast exist, only then a cycle may exist
            slow = slow.next # increments slow by one node
            fast=fast.next.next # increments fast by two nodes

            if slow == fast: # if the fast and slow wvey points to the same node , it means there is a cycle
                return True

        return False