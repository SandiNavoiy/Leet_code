# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''''''
        if head == None:
            return None
        temp_arr = []
        temp = head
        while temp is  not None:
            temp_arr.append(temp.val)
            temp = temp.next

        temp_arr.sort()
        temp = head
        i = 0

        while temp is not None:
            temp.val = temp_arr[i]

            i = i + 1
            temp = temp.next
        return head
