class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        """"""
        new = 0
        for i in range(len(nums)):
            ind = format(i, "b")
            if ind.count("1") == k:
                new += nums[i]
        return new


nums = [5, 10, 1, 5, 2]
k = 1
s = Solution()
print(s.sumIndicesWithKSetBits(nums, k))
