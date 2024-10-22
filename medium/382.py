# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        count, output = 0, 0
        curr = self.head
        while curr != None:
            count += 1
            if random.randint(1, count) == 1:
                output = curr.val
            curr = curr.next
        return output


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
