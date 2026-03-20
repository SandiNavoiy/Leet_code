from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """"""
        max_num = max(nums)
        return sum(max_num - num for num in nums)
s = Solution()
print(s.minMoves([1,2,3]))
