from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        """"""
        minn = min(nums)
        maxx = max(nums)
        return [i for i in range(minn, maxx+1) if i not in nums]


s = Solution()
print(s.findMissingElements([1,4,2,5]))
