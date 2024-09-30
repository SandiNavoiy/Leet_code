class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        """"""
        for i in range(k):
            mm = nums.index(min(nums))
            nums[mm] = nums[mm] * multiplier

        return nums


nums = [2, 1, 3, 5, 6]
k = 5
multiplier = 2
s = Solution()
print(s.getFinalState(nums, k, multiplier))
