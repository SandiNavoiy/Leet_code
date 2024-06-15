class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        """"""
        n = len(nums)
        ss = sum(nums)
        new = [0 for i in range(n)]
        left_sum = 0
        right_sum = ss
        for i in range(n):
            new[i] = (i * nums[i] - left_sum) + (right_sum - (n - i) * nums[i])
            left_sum = left_sum + nums[i]
            right_sum = right_sum - nums[i]

        return new


nums = [2, 3, 5]
s = Solution()
print(s.getSumAbsoluteDifferences(nums))
