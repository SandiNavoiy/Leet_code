# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """"""

        if head == None or head.next == None:
            return head

        # temp = ListNode(0)
        # temp.next = head
        # cur = temp
        # while cur.next and cur.next.next:
        #     temp1 = cur.next
        #     temp2 = cur.next.next
        #     cur.next = temp2
        #     temp1.next = temp2.next
        #     temp2.next = temp1
        #     cur = cur.next.next
        # return temp.next


head = [1, 2, 3, 4]
