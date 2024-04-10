class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        """"""
        n = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if j > i and nums[i] < nums[j]:
                    if nums[j] - nums[i] > n:
                        n = nums[j] - nums[i]
        if n == 0:
            return -1
        return n


nums = [7, 1, 5, 4]
s = Solution()
print(s.maximumDifference(nums))
