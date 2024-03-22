import collections


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        """Степень массива"""
        l = dict(collections.Counter(nums))
        count = max(l.values())



        return count


nums = [1,2,2,3,1]
s = Solution()
print(s.findShortestSubArray(nums))
