# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        sss = []
        cur = head
        while cur:
            sss.append(cur.val)
            cur = cur.next
        return sss == sss[::-1]
