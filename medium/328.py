# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        chet = []
        nechet = []
        i = 0
        cur = head
        while cur:
            if i % 2 == 0:
                chet.append(cur.val)
            else:
                nechet.append(cur.val)
            i = i + 1
            cur = cur.next
        rez = chet + nechet
        cur = head
        i = 0
        while cur:
            cur.val = rez[i]
            i = i + 1
            cur = cur.next

        return head


