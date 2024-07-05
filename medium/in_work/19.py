# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ''''''
        cur  = head
        len_head = 1
        if cur.next is None:
            return None
            # Если нужно удалить первый элемент

        while cur.next:
            cur = cur.next
            len_head = len_head + 1
        if len_head == n:
            return head.next
        cur = head
        i = 1
        while cur.next:

            if i  == len_head - n:
                cur.next = cur.next.next
                break
            cur = cur.next
            i = i + 1



        return head


