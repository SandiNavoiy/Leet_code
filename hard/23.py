# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        """"""
        new = []
        for i in lists:
            cur = i
            while cur:
                new.append(cur.val)
                cur = cur.next
        new.sort()
        head = ListNode()
        cur = head

        for i in new:
            cur.next = ListNode(i)
            cur = cur.next

        return head.next
