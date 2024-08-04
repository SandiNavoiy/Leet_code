# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Merge two lists"""

        arr = []
        rez = None
        cur1 = list1
        cur2 = list2

        while cur1:
            arr.append(cur1.val)
            cur1 = cur1.next

        while cur2:
            arr.append(cur2.val)
            cur2 = cur2.next

        arr.sort(reverse=True)

        for i in arr:
            rez = ListNode(i, rez)

        return rez
