# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        """"""
        count = 0
        cur = list1
        while count < a - 1:
            cur = cur.next
            count = count + 1
        a_list = cur
        while count < b + 1:
            cur = cur.next
            count = count + 1
        a_list.next = list2
        next2 = list2
        while next2.next is not None:
            next2 = next2.next
        next2.next = cur

        return list1
