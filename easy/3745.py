from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:

        """Максимизировать выражение трех элементов."""
        nums.sort()

        return nums[-1] + nums[-2] - nums[0]


