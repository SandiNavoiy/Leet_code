# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        head_node = head
        number = ""
        while head_node:
            number += str(head_node.val)
            head_node = head_node.next
        return int(number, 2)