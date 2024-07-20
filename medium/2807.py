# Definition for singly-linked list.
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''''''
        cur = head

        while cur.next:
            t = ListNode(math.gcd(cur.val, cur.next.val))
            t.next = cur.next
            cur.next = t
            cur = cur.next.next
        return head
