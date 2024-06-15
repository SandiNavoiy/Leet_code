# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None or head.node is None:
            return head
        current = head
        while current.node is not None:
            if current.next.val  == val:
                current.next = current.next.next
