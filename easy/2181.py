# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Mer"""
        cur = head
        while True:
            if cur.next.val == 0 and cur.next.next == None:
                cur.next = None
                break
            if cur.next.val == 0:
                cur = cur.next
            cur.val = cur.val + cur.next.val
            cur.next = cur.next.next

        return head
