from typing import List
class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        """Максимизировать сумму не более чем K различных элементов."""
        lst = sorted(set(nums), reverse=True)
        return lst[:k]


s = Solution()
print(s.maxKDistinct([84,93,100,77,90], 3))
