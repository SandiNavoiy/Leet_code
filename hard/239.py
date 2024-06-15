from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """"""
        if not nums:
            return []

        deq = deque()
        result = []
        for i in range(len(nums)):
            if deq and deq[0] == i - k:
                deq.popleft()
            while deq and deq[-1] < nums[i]:
                deq.pop()

            deq.append(i)
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
s = Solution()
print(s.maxSlidingWindow(nums, k))
