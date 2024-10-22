# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """"""
        rez = []
        cur = head
        while cur:
            rez.append(cur.val)
            cur = cur.next
        cur = head
        rez[left - 1 : right] = rez[left - 1 : right][::-1]
        cur = head
        i = 0
        while cur:
            cur.val = rez[i]
            cur = cur.next
            i += 1

        return head
