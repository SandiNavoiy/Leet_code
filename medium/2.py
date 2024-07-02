# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """"""
        head = ListNode()
        cur = head
        carry = 0
        while l1 or l2 or carry != 0:
            if l1:
                l1_value = l1.val
            else:
                l1_value = 0
            if l2:
                l2_value = l2.val
            else:
                l2_value = 0
            summ = l1_value + l2_value + carry
            cur.next = ListNode(summ % 10)
            carry = summ // 10
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None

            cur = cur.next
        return head.next
