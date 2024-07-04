# Definition for singly-linked list.
from typing import Optional


class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fin  = head
        while fin and fin.next:
            head = head.next
            fin = fin.next.next
        return head

