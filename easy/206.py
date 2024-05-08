from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_node = head
        prev_node = None

        while head_node:
            next_node = head_node.next
            head_node.next = prev_node
            prev_node = head_node
            head_node = next_node
        return prev_node
