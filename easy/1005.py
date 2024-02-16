class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        """"""
        while k > 0:
            x = nums.index(min(nums))
            nums[x] = nums[x] * -1
            k = k - 1
        return sum(nums)


nums = [-4, 2, 3]
k = 1
s = Solution()
print(s.largestSumAfterKNegations(nums, k))
