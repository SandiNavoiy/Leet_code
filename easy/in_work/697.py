from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        """Степень массива"""
        c = defaultdict(list)
        for i, j in enumerate(nums):
            c[j].append(i)
        degree = max([len(x) for x in c.values()])
        return dict(c), degree


nums = [1, 2, 2, 3, 1]
s = Solution()
print(s.findShortestSubArray(nums))
