# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        """"""
        temp = set()
        cur = headA
        while cur:
            temp.add(cur)
            cur = cur.next

        cur = headB
        while cur:
            if cur in temp:
                return cur
            cur = cur.next
        return None
