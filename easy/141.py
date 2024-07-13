# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sl = head
        fast = head
        while fast and fast.next:
            sl = sl.next
            fast = fast.next.next

            if fast == sl:
                return True
        return False
