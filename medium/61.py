# Definition for singly-linked list.
from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """"""
        rez = deque()
        cur = head
        while cur:
            rez.append(cur.val)
            cur = cur.next
        rez.rotate(k)
        cur = head
        i = 0
        while cur:
            cur.val = rez[i]
            cur = cur.next
            i = i + 1
        return head
