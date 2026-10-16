from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        """Наименьшее недостающее кратное K"""
        step = k
        while k in nums:
            k = k + step

        return k



s = Solution()
print(s.missingMultiple([8,2,3,4,6], 2))
