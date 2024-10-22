# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """"""
        cur = head
        fin = head
        pref = head
        if cur.next is None:
            return None
        while fin and fin.next:
            pref = cur
            cur = cur.next
            fin = fin.next.next
        pref.next = cur.next
        return head
